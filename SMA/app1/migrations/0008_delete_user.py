# Generated by Django 4.1.3 on 2022-12-08 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]