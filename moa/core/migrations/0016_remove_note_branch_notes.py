# Generated by Django 4.2.11 on 2024-06-11 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_note_branch_notes_alter_note_seed_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='branch_notes',
        ),
    ]
