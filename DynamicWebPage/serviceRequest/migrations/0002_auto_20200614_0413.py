# Generated by Django 3.0.7 on 2020-06-14 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceRequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowfacility',
            name='startTime',
            field=models.DateTimeField(),
        ),
    ]
