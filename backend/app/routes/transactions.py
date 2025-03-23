from flask import Blueprint
from .. services.transaction_service import *

bp = Blueprint('transactions', __name__, url_prefix='/api/transaction')

# get qr code for payment
@bp.route('/pay', methods=['GET'])
def get_comments():
    return {"status":"ok"}

@bp.route('/history', methods=['GET'])
def get_rates():
    return {"status":"ok"}