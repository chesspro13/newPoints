# Generated by Django 2.0.7 on 2021-01-01 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointRequests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointrequest',
            name='date',
            field=models.CharField(default='today', max_length=9),
            preserve_default=False,
        ),
    ]
