from core.automations import run_email_automation
from core.brain import think

def process_task(task):

    if task.type == "email":
        return run_email_automation(task.data)

    if task.type == "analysis":
        return think(task.data)

    return "unknown task"
