from flask import Blueprint
from .. services.reputation_service import *

bp = Blueprint('reputaions', __name__, url_prefix='/api/reputation')

@bp.route('/comments', methods=['GET'])
def get_comments():
    return {"status":"ok"}

@bp.route('/rates', methods=['GET'])
def get_rates():
    return {"status":"ok"}