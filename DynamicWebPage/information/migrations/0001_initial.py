# Generated by Django 3.0.7 on 2020-06-14 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('coverImage', models.URLField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'information',
            },
        ),
    ]