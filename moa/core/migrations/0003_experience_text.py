# Generated by Django 4.2.11 on 2024-04-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_experience_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
