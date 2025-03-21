import os

jwt_config = {
    'JWT_SECRET': os.getenv('JWT_SECRET', os.urandom(16).hex()),
    'JWT_ALG': os.getenv('JWT_ALG', 'HS256')
}

mail_service_config = {
    'email': '',
    'key': ''
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