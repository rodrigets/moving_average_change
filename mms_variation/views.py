from datetime import datetime, timedelta
import json
import pytz
from django.http import HttpResponse, response
from rest_framework.views import APIView
from .models import MmsVariation
from .tasks import get_candle_first_to_save


class MmsVariationView(APIView):
    def post(self, request):
        """Responsible for creating trigger the first load of records in the database

        Returns:
            [Response]: Returns whether data was generated successfully or previously
        """

        try:
            if MmsVariation.objects.all().exists():
                return HttpResponse(
                    "First synchronization done previously", status=200
                )

            get_candle_first_to_save(365)
            return HttpResponse("First successful synchronization", status=200)

        except Exception as ex:
            return HttpResponse(f"errors:{str(ex)}", status=500)

    def get(self, request):
        """Returns data list according to parameters

        Args:
            pair: desired pair(BRLBTC or BRLETH)
            from: start date in timestamp
            to: final date in timestamp
            range: desired number of days for mms (20, 50 or 200)

        Returns:
            [Reponse]: data list according to parameters
        """

        try:
            utc = pytz.UTC
            list_return = []
            pair = self.request.query_params.get("pair", "")
            timestamp_from = self.request.query_params.get("from", "")
            timestamp_to = self.request.query_params.get("to", "")
            range = self.request.query_params.get("range", "")

            if not pair or not timestamp_from or not timestamp_to or not range:
                return response.JsonResponse(
                    data={
                        "error": "It is necessary to inform all parameters(pair, from, to, range)"
                    },
                    status=500,
                )

            if pair not in ["BRLBTC", "BRLETH"]:
                return response.JsonResponse(
                    data={
                        "error": "The parameter pair needs to be entered as BRLBTC or BRLETH"
                    },
                    status=500,
                )
            if range not in ["20", "50", "200"]:
                return response.JsonResponse(
                    data={
                        "error": "The parameter range needs to be entered as 20, 50 or 200"
                    },
                    status=500,
                )

            datetime_from = utc.localize(
                datetime.fromtimestamp(int(timestamp_from))
            )
            datetime_to = utc.localize(
                datetime.fromtimestamp(int(timestamp_to))
            )

            if datetime_from < utc.localize((datetime.now() - timedelta(365))):
                return response.JsonResponse(
                    data={
                        "error": "The from parameter cannot be less than 365 days"
                    },
                    status=500,
                )

            object = MmsVariation.objects.filter(pair=pair)

            for obj in object:
                if (
                    obj.timestamp > datetime_from
                    and obj.timestamp < datetime_to
                ):
                    if range == "20":
                        list_return.append(
                            {
                                "timestamp": int(
                                    datetime.timestamp(obj.timestamp)
                                ),
                                "mms": obj.mms_20,
                            }
                        )
                    if range == "50":
                        list_return.append(
                            {
                                "timestamp": int(
                                    datetime.timestamp(obj.timestamp)
                                ),
                                "mms": obj.mms_50,
                            }
                        )
                    if range == "200":
                        list_return.append(
                            {
                                "timestamp": int(
                                    datetime.timestamp(obj.timestamp)
                                ),
                                "mms": obj.mms_200,
                            }
                        )
            return response.JsonResponse(data={"data": list_return}, status=200)

        except Exception as ex:
            return response.JsonResponse(data={"error": str(ex)}, status=500)
