# Generated by Django 4.2.11 on 2024-04-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tag_experience_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('explanation', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.AddField(
            model_name='experience',
            name='identites',
            field=models.ManyToManyField(to='core.identity'),
        ),
    ]
