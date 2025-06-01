import os
import random


port = 80
schema = 'http' if port != 443 else 'https'
host = '127.0.0.1'
site_url = f'{schema}://{host}:{port}' if port != 80 and port != 443 else f'{schema}://{host}'


jwt_config = {
    'JWT_SECRET': os.getenv('JWT_SECRET', os.urandom(16).hex()),
    'JWT_ALG': os.getenv('JWT_ALG', 'HS256'),
    "JWT_EXP_DELTA_SECONDS": 3600
}

mail_service_config = {
    'email': 'mail.service.lqc@gmail.com',
    'key': 'xhef avfg bzye riun'
}

oauth2_config = {
    'client_id': os.getenv('OAUTH2_CLIENT_ID', '957032210822-4v67c9lvii451v6i4djg4qr098h8vsqd.apps.googleusercontent.com'),
    'client_secret': os.getenv('OAUTH2_CLIENT_SECRET', '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'),
    'grant_type': os.getenv('OAUTH2_GRANT_TYPE', 'authorization_code')
}

db_config = {
    'pguser': os.getenv('DB_USER', 'root'),
    'pgpassword': os.getenv('DB_PASS', 'root'),
    'pghost': os.getenv('DB_HOST', 'db'),
    'pgport': os.getenv('DB_PORT', '5432'),
    'pgdb': os.getenv('DB_NAME', 'shop'),
    'poolsize': 50,
    'debug': False
}

app_config = {
    'JSONIFY_PRETTYPRINT_REGULAR': False,
    'JSON_SORT_KEYS': False,
    'DEBUG': False
}

history_config = {
    'TRANSACTION_SALT': random.randbytes(4)
}

bot_config = {
    'AYD_API_KEY': os.getenv('AYD_API_KEY', '2340192752971870818e633fbafd6139faa4bea34357e376d5a2113c45311685'),
    'AYD_CHATBOT_ID': os.getenv('AYD_CHATBOT_ID', 'b82b045ee911f0ae5e16ce4ae9bd4256'),
    'AYD_SESSION_INIT_URL': os.getenv('AYD_SESSION_INIT_URL', 'https://www.askyourdatabase.com/api/chatbot/v2/session'),
    'AYD_ASK_URL': os.getenv('AYD_ASK_URL', 'https://www.askyourdatabase.com/api/ask?debug=false')
}

momo_config = {
    "redirect_url": os.getenv('MOMO_REDIRECT_URL', f'{site_url}/api/transaction/confirm'),
    "ipn_url": os.getenv('MOMO_IPN_URL', f'{site_url}/api/transaction/confirm'),
    "endpoint": os.getenv('MOMO_ENDPOINT', 'https://test-payment.momo.vn/v2/gateway/api/create'),
}