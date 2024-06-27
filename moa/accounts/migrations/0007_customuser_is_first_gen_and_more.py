# Generated by Django 4.2.11 on 2024-06-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_experience_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_first_gen',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_international_student',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
