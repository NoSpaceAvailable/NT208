from datetime import datetime, timezone

def get_current_time() -> str:
    local_time = datetime.now()
    utc_time = local_time.astimezone(timezone.utc)
    return utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")