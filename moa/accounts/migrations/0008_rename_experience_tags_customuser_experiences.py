# Generated by Django 4.2.11 on 2024-06-29 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_is_first_gen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='experience_tags',
            new_name='experiences',
        ),
    ]
