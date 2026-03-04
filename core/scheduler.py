import time
from database.db import SessionLocal
from database.models import Task
from core.agent import process_task

def run_scheduler():

    while True:

        db = SessionLocal()

        tasks = db.query(Task).filter(Task.status == "pending").all()

        for task in tasks:

            process_task(task)

            task.status = "completed"

            db.commit()

        time.sleep(10)
