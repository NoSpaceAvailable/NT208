import os

jwt_config = {
    'JWT_SECRET': os.getenv('JWT_SECRET', os.urandom(16).hex()),
    'JWT_ALG': os.getenv('JWT_ALG', 'HS256'),
    "JWT_EXP_DELTA_SECONDS": 3600
}

mail_service_config = {
    'email': 'mail.service.lqc@gmail.com',
    'key': 'xhef avfg bzye riun'
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
    'JSON_SORT_KEYS': False
}

gemini_config = {
    'API_KEY': os.getenv('GEMINI_API_KEY', 'foo')
}