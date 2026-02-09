from pydantic import BaseModel


class CurrencyRates(BaseModel):
    USD: float
    EUR: float
    RUB: float
    CNY: float