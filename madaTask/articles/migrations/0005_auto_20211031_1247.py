# Generated by Django 3.2.8 on 2021-10-31 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='cregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.IntegerField(default=0)),
                ('customerFirstName', models.CharField(max_length=30)),
                ('customerLastName', models.CharField(max_length=100)),
                ('customerServicelevel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='eregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sName', models.CharField(max_length=30)),
                ('sID', models.CharField(max_length=30)),
                ('slevel', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
