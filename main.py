import threading
from bot.telegram_bot import run_bot
from core.scheduler import run_scheduler

def start():

    bot_thread = threading.Thread(target=run_bot)
    scheduler_thread = threading.Thread(target=run_scheduler)

    bot_thread.start()
    scheduler_thread.start()

if __name__ == "__main__":
    start()
