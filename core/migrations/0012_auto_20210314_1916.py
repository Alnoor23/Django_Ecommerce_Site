# Generated by Django 3.1.7 on 2021-03-14 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210314_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='name',
        ),
    ]
