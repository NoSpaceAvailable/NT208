from app import app
from app.global_config import app_config

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=app_config['DEBUG'])