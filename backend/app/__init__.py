from flask import Flask
from flask_cors import CORS
from .global_config import app_config

app = Flask(__name__)
app.config.from_object(app_config)
CORS(app)

from .routes import auth, products, transactions, reputation, healthcheck
app.register_blueprint(auth.bp)
app.register_blueprint(products.bp)
app.register_blueprint(transactions.bp)
app.register_blueprint(reputation.bp)
app.register_blueprint(healthcheck.bp)