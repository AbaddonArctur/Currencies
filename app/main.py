import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.config import APP_NAME, WS_UPDATE_INTERVAL
from app.services.nbrb import fetch_rates
from app.ws.manager import ConnectionManager

app = FastAPI(
    title=APP_NAME,
    version="1.0.0",
)

manager = ConnectionManager()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()


@app.websocket("/ws/rates")
async def rates_ws(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            rates = await fetch_rates()
            await manager.send_json(rates.model_dump(), websocket)
            await asyncio.sleep(WS_UPDATE_INTERVAL)
    except WebSocketDisconnect:
        manager.disconnect(websocket)