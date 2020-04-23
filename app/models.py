"""
app.models.py
"""
from pydantic import BaseModel


class LatestResponse(BaseModel):
    """
    Latest model.
    """
    confirmed: int
    recovered: int
    deaths: int
    last_updated: str
