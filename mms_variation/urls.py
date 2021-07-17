from django.urls import path
from .views import MmsVariationView
import os

VERSION = os.environ["VERSION"]

urlpatterns = [
    path(
        f"{VERSION}/mms-variation/",
        MmsVariationView.as_view(),
        name="mms-variation",
    ),
]
