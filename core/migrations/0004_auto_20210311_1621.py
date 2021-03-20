# Generated by Django 3.1.7 on 2021-03-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='phonenumber',
            field=models.IntegerField(default=0),
        ),
    ]
