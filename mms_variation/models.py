from django.db import models


class MmsVariation(models.Model):

    pair = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="Pair"
    )

    timestamp = models.DateTimeField(verbose_name="Timestamp")

    mms_20 = models.FloatField(verbose_name="MMS 20", null=True, blank=True)

    mms_50 = models.FloatField(verbose_name="MMS 50", null=True, blank=True)

    mms_200 = models.FloatField(verbose_name="MMS 200", null=True, blank=True)

    def __str__(self):
        return f"{self.pair}"

    class Meta:
        verbose_name = "Mms Variation"
        verbose_name_plural = "Mms Variations"
        ordering = [
            "-timestamp",
        ]
