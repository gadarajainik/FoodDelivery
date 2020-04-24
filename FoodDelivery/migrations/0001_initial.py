# Generated by Django 2.1.7 on 2019-03-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='py_user_details',
            fields=[
                ('username', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateField()),
                ('mobile', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
    ]
