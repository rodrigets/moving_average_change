import json
from django.test import TestCase
from .models import MmsVariation
from .tasks import calc_first_mms_records
from .cron import calc_daily_mms_records
from .dict_test import dict_task_test


class TasksTestCase(TestCase):
    def test_calc_mms_records(self):
        calc_first_mms_records("BRLBTC", dict_task_test)
        records = MmsVariation.objects.all()
        last_record_btc = MmsVariation.objects.filter(pair="BRLBTC").order_by(
            "-id"
        )[0]
        self.assertEqual(len(records), 400)
        self.assertEqual(last_record_btc.mms_20, 20)
        self.assertEqual(last_record_btc.mms_50, 20)
        self.assertEqual(last_record_btc.mms_200, 15)

        new_dict = dict_task_test.get("candles")
        new_dict.append({"timestamp": 1625961600, "close": 100})

        calc_daily_mms_records("BRLBTC", {"candles": new_dict})
        new_record = MmsVariation.objects.filter(pair="BRLBTC").order_by("-id")[
            0
        ]
        self.assertEqual(round(new_record.mms_20, 2), 24)
        self.assertEqual(round(new_record.mms_50, 2), 21.6)
        self.assertEqual(round(new_record.mms_200, 2), 15.45)
