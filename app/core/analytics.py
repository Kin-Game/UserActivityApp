import pandas as pd
from app.core.database import DB_PATH

def load_data():
    if not DB_PATH.exists():
        return pd.DataFrame(columns=["timestamp", "process_name", "window_title", "duration"])

    df = pd.read_csv(DB_PATH)  # TODO: later replace with proper SELECT
    return df
