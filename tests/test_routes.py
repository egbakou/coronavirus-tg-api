from pprint import pformat as pf


async def test_cases_overview(async_api_client):
    response = await async_api_client.get("/v1/cases")

    print(f"GET {response.url}\n{response}")

    response_json = response.json()
    print(f"\tjson:\n{pf(response_json)}")

    assert response.status_code == 200
    assert response_json["confirmed"]
    assert response_json["recovered"]
    assert response_json["deaths"]
    assert response_json["last_updated"]


async def test_get_confirmed_data(async_api_client):
    response = await async_api_client.get("/v1/cases/confirmed")

    print(f"GET {response.url}\n{response}")

    response_json = response.json()
    print(f"\tjson:\n{pf(response_json)}")

    assert response.status_code == 200
    assert response_json["confirmed"]
    assert response_json["last_updated"]


async def test_get_recovered_data(async_api_client):
    response = await async_api_client.get("/v1/cases/recovered")

    print(f"GET {response.url}\n{response}")

    response_json = response.json()
    print(f"\tjson:\n{pf(response_json)}")

    assert response.status_code == 200
    assert response_json["recovered"]
    assert response_json["last_updated"]


async def test_get_deaths_data(async_api_client):
    response = await async_api_client.get("/v1/cases/deaths")

    print(f"GET {response.url}\n{response}")

    response_json = response.json()
    print(f"\tjson:\n{pf(response_json)}")

    assert response.status_code == 200
    assert response_json["deaths"]
    assert response_json["last_updated"]


async def test_get_sources(async_api_client):
    response = await async_api_client.get("/v1/sources")

    print(f"GET {response.url}\n{response}")

    response_json = response.json()
    print(f"\tjson:\n{pf(response_json)}")

    assert response.status_code == 200
