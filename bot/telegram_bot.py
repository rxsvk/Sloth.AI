from telegram.ext import ApplicationBuilder, CommandHandler
from database.db import SessionLocal
from database.models import Session, Task
from core.brain import think
from config import TELEGRAM_TOKEN

async def start(update, context):

    user = update.effective_user.username

    db = SessionLocal()

    s = Session(user=user, service="telegram", status="active")

    db.add(s)
    db.commit()

    await update.message.reply_text("🦥 SLOTH AI activated.")


async def ask(update, context):

    prompt = " ".join(context.args)

    reply = think(prompt)

    await update.message.reply_text(reply)


async def task(update, context):

    text = " ".join(context.args)

    db = SessionLocal()

    t = Task(type="analysis", data=text, status="pending")

    db.add(t)
    db.commit()

    await update.message.reply_text("Task added.")


async def sessions(update, context):

    db = SessionLocal()

    sessions = db.query(Session).all()

    msg = ""

    for s in sessions:
        msg += f"{s.service} : {s.status}\n"

    await update.message.reply_text(msg)


def run_bot():

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(CommandHandler("task", task))
    app.add_handler(CommandHandler("sessions", sessions))

    app.run_polling()
