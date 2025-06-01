from flask import Blueprint, request
from app.services.bot_service import init_bot, ask

bp = Blueprint('bot', __name__, url_prefix='/api/bot')
init_bot()

@bp.route('/ask', methods=['POST'])
def ask_bot():
    data = request.json.get('question')
    if not data:
        return {"status": "error", "bot_answer": "Missing question"}, 400
    try:
        return {"status": "ok", "bot_answer": ask(data)}
    except Exception:
        return {"status": "error", "bot_answer": "Bot is not available"}