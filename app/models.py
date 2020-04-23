"""
app.models.py
"""
from pydantic import BaseModel


class CasesResponse(BaseModel):
    """
    Response for cases data endpoint
    """

    confirmed: int
    recovered: int
    deaths: int
    last_updated: str


class ConfirmedResponse(BaseModel):
    """
    Response for confirmed data endpoint
    """

    confirmed: int
    last_updated: str


class RecoveredResponse(BaseModel):
    """
    Response for recovered data endpoint
    """

    recovered: int
    last_updated: str


class DeathsResponse(BaseModel):
    """
    Response for deaths data endpoint
    """

    deaths: int
    last_updated: str


class SourcesResponse(BaseModel):
    """
    Response for sources data endpoint
    """

    government_website: str
    tracker_api_project: str
