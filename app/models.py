"""
app.models.py
"""
from pydantic import BaseModel


class Latest(BaseModel):
    """
    Latest model.
    """
    confirmed: int
    deaths: int
    recovered: int
    active_cases: int
    last_updated: str


class LatestResponse(BaseModel):
    """
    Response for latest.
    """

    latest: Latest
