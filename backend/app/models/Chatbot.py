from app.global_config import bot_config
import time
import requests
import json


class AlmaBot:
    def __init__(self):
        self.ayd_session_data = {
            "access_token": None,
            "expires_at": 0
        }
        self.ayd_api_key = bot_config['AYD_API_KEY']
        self.ayd_chatbot_id = bot_config['AYD_CHATBOT_ID']
        self.ayd_session_init_url = bot_config['AYD_SESSION_INIT_URL']
        self.ayd_ask_url = bot_config['AYD_ASK_URL']


    def get_access_token(self):
        
        if self.ayd_session_data["access_token"] and time.time() < self.ayd_session_data["expires_at"]:
            return self.ayd_session_data["access_token"]
        
        if not self.ayd_api_key or not self.ayd_chatbot_id:
            raise ValueError("AYD_API_KEY and AYD_CHATBOT_ID must be set in the environment variables.")

        try:
            session_init_payload = {
                "chatbotid": self.ayd_chatbot_id,
                "name": "Alma",
                "email": "alma@example.com"
            }
            headers_inti = {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.ayd_api_key}'
            }
            init_response = requests.post(self.ayd_session_init_url, json=session_init_payload, headers=headers_inti)
            init_response.raise_for_status()

            init_data = init_response.json()
            callback_url = init_data.get('url')

            if not callback_url:
                raise ValueError("No callback URL returned from session initialization.")
            
            callback_response = requests.get(
                callback_url, 
                allow_redirects=False, 
                headers={
                    'Accept': 'application/json, text/plain, */*',
                    'Cookie': f'accessToken={self.ayd_session_data["access_token"]}'
                }
            )

            if not (300 <= callback_response.status_code < 400 and 'Set-Cookie' in callback_response.headers):
                raise ValueError(f"Callback URL returned unexpected status code: {callback_response.status_code}")
            
            set_cookie_header = callback_response.headers.get('Set-Cookie')
            access_token_cookie = None
            for cookie in set_cookie_header.split(';'):
                if 'accessToken' in cookie:
                    access_token_cookie = cookie.split('=')[1].strip()
                    break

            if not access_token_cookie:
                raise ValueError("No access token found in Set-Cookie header.")
            
            self.ayd_session_data["access_token"] = access_token_cookie
            print(f"Access token obtained: {self.ayd_session_data['access_token']}")

            max_age = None
            for cookie in set_cookie_header.split(';'):
                if 'Max-Age' in cookie.lower():
                    try:
                        max_age = int(cookie.split('=')[1].strip())
                        break
                    except ValueError:
                        pass

            if max_age:
                self.ayd_session_data["expires_at"] = time.time() + max_age - (5 * 60)
            else:
                self.ayd_session_data["expires_at"] = time.time() + (7 * 24 * 60 * 60) - (5 * 60)
            
            return self.ayd_session_data["access_token"]
        
        except Exception as e:
            raise Exception(f"Error obtaining AYD access token: {e}")


    def generate_answer(self, question: str) -> str:
        try:
            access_token = self.get_access_token()

            ask_payload = {
                "question": question,
                "botid": self.ayd_chatbot_id,
                "debug": False
            }
            ask_headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json, text/plain, */*',
                'Cookie': f'accessToken={access_token}',
                'Origin': 'https://www.askyourdatabase.com',
                'Referer': f'https://www.askyourdatabase.com/chatbot/{self.ayd_chatbot_id}'
            }

            print(f"Asking AYD: {self.ayd_ask_url}")
            ask_response = requests.post(self.ayd_ask_url, json=ask_payload, headers=ask_headers)
            ask_response.raise_for_status()

            bot_answer = ""
            raw_data = []

            for line in ask_response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        data = decoded_line[5:].strip()
                        try:
                            data_chunk = json.loads(data)
                            raw_data.append(data_chunk)
                            if data_chunk.get("isText") and "content" in data_chunk:
                                bot_answer += data_chunk["content"]
                        except Exception as e:
                            print(f"Error decoding JSON: {e}")
                            continue

            return bot_answer

        except Exception as e:
            print(f"Error during AYD request: {e}")