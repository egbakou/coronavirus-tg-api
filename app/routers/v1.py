"""app.routers.v1.py"""
from fastapi import APIRouter, HTTPException

from ..models import LatestResponse
from ..services.covidgouvtg import fetch_data

V1 = APIRouter()

# Base URL for fetching data.
BASE_URL = "https://covid19.gouv.tg"
# API Project on Github
CURRENT_API_PROJECT_URL = "https://github.com/egbakou/coronavirus-tg-api"


@V1.get("/latest", response_model=LatestResponse)
async def get_latest():
    """
        Getting total of confirmed cases, deaths, recovered, active cases and the last
        updated date.
    """
    data = await fetch_data()
    if data:
        return data
    else:
        raise HTTPException(status_code=404,
                            detail="No data found ! Government website structure is probably changed.")


@V1.get("/sources")
async def get_sources():
    """
    Getting data-sources: Government website and the tracker api project
    """
    return {"gouv_tg": BASE_URL,
            "tracker_api": CURRENT_API_PROJECT_URL}
