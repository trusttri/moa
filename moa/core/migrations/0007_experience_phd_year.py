# Generated by Django 4.2.11 on 2024-05-28 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_experience_first_gen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='phd_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
