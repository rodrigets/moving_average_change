import json
import logging
import os
import requests
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def consult_candle_btc(timestamp_now, timestamp_past):
    """Responsible for querying and returning data BTC from the api MB

    Args:
        timestamp_now ([timestamp]): timestamp of now
        timestamp_past ([timestamp]): origin timestamp

    Returns:
        [json]: Json with data returned from the api
    """

    BRLBTC = os.environ["BRLBTC"]
    try:
        url_btc = (
            f"{BRLBTC}from={timestamp_past}&to={timestamp_now}&precision=1d"
        )
        retorno = requests.request("GET", url=url_btc)
        return json.loads(retorno.text)

    except Exception as ex:
        logger.error(f"Error to consult candle: {str(ex)}")
        return HttpResponse("error: ERROR Sync")


def consult_candle_eth(timestamp_now, timestamp_past):
    """Responsible for querying and returning data ETH from the api MB

    Args:
        timestamp_now ([timestamp]): timestamp of now
        timestamp_past ([timestamp]): origin timestamp

    Returns:
        [json]: Json with data returned from the api
    """

    BRLETH = os.environ["BRLETH"]
    try:
        url_eth = (
            f"{BRLETH}from={timestamp_past}&to={timestamp_now}&precision=1d"
        )
        retorno = requests.request("GET", url=url_eth)
        return json.loads(retorno.text)

    except Exception as ex:
        logger.error(f"Error to consult candle: {str(ex)}")
        return HttpResponse("error: ERROR Sync")
