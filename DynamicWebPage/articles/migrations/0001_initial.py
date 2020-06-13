# Generated by Django 3.0.7 on 2020-06-13 13:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kanban',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('description', models.URLField(blank=True)),
            ],
            options={
                'db_table': 'kanban',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=100)),
                ('lastEditAccount', models.CharField(max_length=100)),
                ('creareDate', models.DateTimeField(auto_now_add=True)),
                ('lastEditDate', models.DateTimeField(auto_now=True)),
                ('title', models.TextField()),
                ('coverImage', models.URLField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('kanban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Kanban')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
