from flask import Flask
from flask_cors import CORS
from .models.Database import Database

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = Database()
print(db.test())
CORS(app)

from .routes import auth, products, transactions, reputation, healthcheck
app.register_blueprint(auth.bp)
app.register_blueprint(products.bp)
app.register_blueprint(transactions.bp)
app.register_blueprint(reputation.bp)
app.register_blueprint(healthcheck.bp)