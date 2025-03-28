from flask import Flask
from flask_cors import CORS
from .global_config import app_config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config.from_object(app_config)
CORS(app)

limiter = Limiter(
    key_func=get_remote_address, 
    app=app,
    default_limits=['100 per minute']
)

from .routes import auth, products, transactions, reputation, healthcheck, bot, profile
app.register_blueprint(bot.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(profile.bp)
app.register_blueprint(products.bp)
app.register_blueprint(reputation.bp)
app.register_blueprint(healthcheck.bp)
app.register_blueprint(transactions.bp)