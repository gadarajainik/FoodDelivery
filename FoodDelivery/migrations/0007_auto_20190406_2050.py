# Generated by Django 2.1.7 on 2019-04-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodDelivery', '0006_auto_20190405_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='image',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=50),
        ),
    ]
