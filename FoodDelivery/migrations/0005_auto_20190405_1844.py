# Generated by Django 2.1.7 on 2019-04-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodDelivery', '0004_auto_20190405_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='image',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AddField(
            model_name='order_details',
            name='name',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AddField(
            model_name='order_details',
            name='price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='quantity',
            field=models.IntegerField(default='0'),
        ),
    ]
