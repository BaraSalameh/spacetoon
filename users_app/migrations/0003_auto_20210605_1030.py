# Generated by Django 2.2.4 on 2021-06-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20210605_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
