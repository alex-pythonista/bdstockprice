# Generated by Django 4.1.3 on 2022-12-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reset_password',
            field=models.BooleanField(default=False),
        ),
    ]
