# Generated by Django 2.0.7 on 2021-01-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_jennifer_pandora_violet'),
    ]

    operations = [
        migrations.CreateModel(
            name='invalid_password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=256)),
                ('task', models.CharField(max_length=1024)),
            ],
        ),
    ]
