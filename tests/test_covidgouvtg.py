import pytest

from app.services import covidgouvtg


@pytest.mark.asyncio
async def test_fetch_data():
    output = await covidgouvtg.fetch_data()
    assert isinstance(output, dict)
    assert output is not None
