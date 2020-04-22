"""
app.models.py
"""
from pydantic import BaseModel


class LatestResponse(BaseModel):
    """
    Latest model.
    """
    confirmed: int
    deaths: int
    recovered: int
    active_cases: int
    last_updated: str
