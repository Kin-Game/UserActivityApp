from datetime import datetime

def format_duration(seconds: int) -> str:
    h, m = divmod(seconds, 3600)
    m, s = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def current_time() -> str:
    return datetime.now().strftime("%H:%M:%S")
