# Generated by Django 4.1.4 on 2023-02-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_customer_phone_alter_customer_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
