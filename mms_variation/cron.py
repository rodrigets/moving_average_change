import numpy
from datetime import datetime, timedelta
from .models import MmsVariation
from .utils import consult_candle_btc, consult_candle_eth


def cron_job_candle_daily():
    """Cron for daily update of records in the table"""

    timestamp_now = int(datetime.timestamp(datetime.now()))
    timestamp_past = int(
        datetime.timestamp(datetime.now() - timedelta(days=200))
    )

    data_btc = consult_candle_btc(timestamp_now, timestamp_past)
    data_eth = consult_candle_eth(timestamp_now, timestamp_past)

    calc_daily_mms_records("BRLBTC", data_btc)
    calc_daily_mms_records("BRLETH", data_eth)


def calc_daily_mms_records(pair, data):
    """Responsible for calculating the average mms of new records

    Args:
        pair: desired pair(BRLBTC or BRLETH)
        data : Json with the MB data list
    """

    mms_20_final = 0
    mms_50_final = 0
    mms_200_final = 0
    m20 = []
    m50 = []
    m200 = []

    for rec in data.get("candles"):
        # mms 20
        m20.append(rec.get("close"))
        if len(m20) == 20:
            mms_20_final = float(numpy.mean(m20))
        if len(m20) > 20:
            del m20[0]
            mms_20_final = float(numpy.mean(m20))

        # mms 50
        m50.append(rec.get("close"))
        if len(m50) == 50:
            mms_50_final = float(numpy.mean(m50))
        if len(m50) > 50:
            del m50[0]
            mms_50_final = float(numpy.mean(m50))

        # mms 200
        m200.append(rec.get("close"))
        if len(m200) == 200:
            mms_200_final = float(numpy.mean(m200))
        if len(m200) > 200:
            del m200[0]
            mms_200_final = float(numpy.mean(m200))

    record_mms = MmsVariation.objects.create(
        pair=pair,
        timestamp=datetime.fromtimestamp(rec.get("timestamp")),
        mms_20=mms_20_final,
        mms_50=mms_50_final,
        mms_200=mms_200_final,
    )
    record_mms.save()
