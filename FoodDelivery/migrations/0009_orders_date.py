# Generated by Django 2.1.7 on 2019-04-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodDelivery', '0008_auto_20190407_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateField(default='2019-04-08'),
        ),
    ]