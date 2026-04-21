from app.db.queries import insert_audit_log


def log_event(signal_id: str, step: str, data: dict):
    try:
        insert_audit_log(signal_id, step, data)
    except Exception as e:
        print(f"[LOG ERROR] {e}")