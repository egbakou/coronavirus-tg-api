from pprint import pformat as pf

import pytest


@pytest.mark.asyncio
async def test_get_sources(async_api_client):
    response = await async_api_client.get("/v1/sources")

    print(f"GET {response.url}\n{response}")

    response_json = response.json()
    print(f"\tjson:\n{pf(response_json)}")

    assert response.status_code == 200
