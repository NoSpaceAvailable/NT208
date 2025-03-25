from flask import Blueprint, request
from ..services.bot_service import init_bot, ask, bot_alive

bp = Blueprint('bot', __name__, url_prefix='/api/bot')
init_bot()

@bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    if bot_alive():
        return {"status": "ok"}
    return {"status": "error"}, 500

@bp.route('/ask', methods=['POST'])
def ask_bot():
    data = request.json.get('question')
    if not data:
        return {"status": "error", "bot_answer": "Missing question"}, 400
    return {"status": "ok", "bot_answer": ask(data)}