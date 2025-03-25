from ..models.Chatbot import AlmaBot

bot = None

def init_bot():
    global bot
    bot = AlmaBot()

def ask(question: str) -> str:
    return bot.generate_answer(question)

def bot_alive() -> bool:
    return bot.health_check()