# Generated by Django 3.0.7 on 2020-06-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200613_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
