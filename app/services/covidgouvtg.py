"""
app.services.covidgouvtg.py
"""
import logging

import dateparser
from aiohttp import ClientConnectionError, ClientHttpProxyError, ClientConnectorSSLError
from bs4 import BeautifulSoup

from ..utils import httputils

LOGGER = logging.getLogger("services.covidgouvtg")

# Base URL for fetching data.
BASE_URL = "https://covid19.gouv.tg"


async def fetch_data():
    """
    Retrieve data about Covid-19 from government official website.

    :return: website data such as confirmed cases, deaths, active cases and recovered.
    :rtype: dict
    """
    try:
        # Request the html page
        LOGGER.info("covid19.gouv.tg Requesting data...")
        async with httputils.CLIENT_SESSION.get(BASE_URL, ssl=False) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
        LOGGER.info(BASE_URL + " html parsed...")

        # Find data in the html code based on tag's id and classes
        elements = soup.find(id='timeinfo').find_all(class_='elementor-heading-title elementor-size-default')
        date_french_string = elements[0].contents[0].split("jour")[1].strip()
        hour_french_string = elements[1].contents[0]
        updated_date = dateparser.parse(date_french_string + ' ' + hour_french_string)
        LOGGER.info(BASE_URL + " Data received...")

        # Normalize data
        active_cases = int(soup.find(id='active-cases').find('h2').contents[0])
        recovered = int(soup.find(id='cured').find('h2').contents[0])
        deaths = int(soup.find(id='deceased').find('h2').contents[0])
        confirmed = int(soup.find(id='total-case').find('h2').contents[0])
        LOGGER.info(BASE_URL + " Data normalized...")

        # Return the final data.
        return {"confirmed": confirmed,
                "recovered": recovered,
                "deaths": deaths,
                "last_updated": updated_date.__str__()}

    # Never Trust HTML
    except (ClientConnectionError, ClientHttpProxyError, ClientConnectorSSLError):
        # ALERT!! Send notification to Admin
        LOGGER.exception("ALERT!! Client Error...")
        return None
    except ValueError:
        # ALERT!! Send notification to Admin
        LOGGER.exception("ALERT!! Conversion error when parsing or normalizing data...")
        return None
