# Generated by Django 3.1.6 on 2021-07-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MmsVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(blank=True, max_length=25, null=True, verbose_name='Pair')),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp')),
                ('mms_20', models.FloatField(blank=True, null=True, verbose_name='MMS 20')),
                ('mms_50', models.FloatField(blank=True, null=True, verbose_name='MMS 50')),
                ('mms_200', models.FloatField(blank=True, null=True, verbose_name='MMS 200')),
            ],
            options={
                'verbose_name': 'Mms Variation',
                'verbose_name_plural': 'Mms Variations',
                'ordering': ['-timestamp'],
            },
        ),
    ]