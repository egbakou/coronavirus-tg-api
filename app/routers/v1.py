"""app.routers.v1.py"""

from fastapi import APIRouter, HTTPException

from ..models import CasesResponse, ConfirmedResponse, DeathsResponse, RecoveredResponse, SourcesResponse
from ..services.covidgouvtg import fetch_data

V1 = APIRouter()

# Base URL for fetching data.
BASE_URL = "https://covid19.gouv.tg"
# API Project on Github
CURRENT_API_PROJECT_URL = "https://github.com/egbakou/coronavirus-tg-api"


@V1.get("/cases", response_model=CasesResponse)
async def get_cases_overview():
    """
        Getting total of confirmed cases, deaths, recovered and the last
        updated date.
    """
    data = await fetch_data()
    print(data)
    if data:
        return data
    raise HTTPException(status_code=404, detail="No data found ! Government website structure is probably changed.")


@V1.get("/cases/confirmed", response_model=ConfirmedResponse)
async def get_confirmed_data():
    """
    Getting confirmed data.
    """
    data = await fetch_data()
    if data:
        return {"confirmed": data["confirmed"], "last_updated": data["last_updated"]}
    raise HTTPException(status_code=404, detail="No data found ! Government website structure is probably changed.")


@V1.get("/cases/recovered", response_model=RecoveredResponse)
async def get_recovered_data():
    """
    Getting recoved data
    """
    data = await fetch_data()
    if data:
        return {"recovered": data["recovered"], "last_updated": data["last_updated"]}
    raise HTTPException(status_code=404, detail="No data found ! Government website structure is probably changed.")


@V1.get("/cases/deaths", response_model=DeathsResponse)
async def get_deaths_data():
    """
    Getting deaths data
    """
    data = await fetch_data()
    if data:
        return {"deaths": data["deaths"], "last_updated": data["last_updated"]}
    raise HTTPException(status_code=404, detail="No data found ! Government website structure is probably changed.")


@V1.get("/sources", response_model=SourcesResponse)
async def get_sources():
    """
    Getting data-sources: Government website and the tracker api project
    """
    return {"government_website": BASE_URL, "tracker_api_project": CURRENT_API_PROJECT_URL}
