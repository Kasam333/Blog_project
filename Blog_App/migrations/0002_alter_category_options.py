# Generated by Django 5.1.4 on 2025-01-17 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
    ]
