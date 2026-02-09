import os

APP_NAME: str = os.environ.get("APP_NAME", "NBRB Currency Monitor")
WS_UPDATE_INTERVAL: int = int(os.environ.get("WS_UPDATE_INTERVAL", "5"))
NBRB_URL: str = os.environ.get(
    "NBRB_URL",
    "https://api.nbrb.by/exrates/rates?periodicity=0",
)
