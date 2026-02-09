import httpx

from app.config import NBRB_URL
from app.schemas import CurrencyRates

CODES = {"USD", "EUR", "RUB", "CNY"}


async def fetch_rates() -> CurrencyRates:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(NBRB_URL)
        response.raise_for_status()

    data = response.json()
    rates: dict[str, float] = {}

    for item in data:
        code = item["Cur_Abbreviation"]
        if code in CODES:
            rates[code] = item["Cur_OfficialRate"]

    return CurrencyRates(**rates)
