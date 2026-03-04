from core.brain import think

def run_email_automation(email):

    decision = think(
        f"Analyze this email and decide whether to reply, schedule a meeting, or ignore.\n\n{email}"
    )

    return decision
