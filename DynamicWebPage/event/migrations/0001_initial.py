# Generated by Django 3.0.7 on 2020-06-13 20:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=100)),
                ('creareDate', models.DateTimeField(auto_now_add=True)),
                ('lastEditDate', models.DateTimeField(auto_now=True)),
                ('eventType', models.CharField(max_length=100)),
                ('context', models.TextField()),
                ('status', models.TextField()),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]
