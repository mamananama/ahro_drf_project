from pathlib import Path
import os
import environ


def get_back_end_url(self):
    BASE_DIR = Path(__file__).resolve().parent
    env = environ.Env()
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    return {"BACK_END_URL": env.str("BACK_END_URL")}
