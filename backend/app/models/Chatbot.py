from .. global_config import gemini_config
from google import genai
from google.genai import types
from .. utils.gemini import example_contents, example_generate_content_config


class AlmaBot:
    def __init__(self):
        self.contents = example_contents
        self.generate_content_config = example_generate_content_config
        self.model = "gemini-2.0-flash-lite"
        self.client = genai.Client(
            api_key=gemini_config["API_KEY"],
        )

    def generate_answer(self, question: str) -> str:
        prepared_question = types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=question),
            ],
        )
        self.contents.append(prepared_question)
        response = ""
        for chunk in self.client.models.generate_content_stream(
            model=self.model,
            contents=self.contents,
            config=self.generate_content_config,
        ):
            response += chunk.text
        return response
    
    def health_check(self) -> bool:
        return True