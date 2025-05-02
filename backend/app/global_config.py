import os
import random

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

gemini_config = {
    'API_KEY': os.getenv('GEMINI_API_KEY', 'AIzaSyBVPmhhWu6ViWJBacgSSzgmPgUScKGxdWg')
}