# Generated by Django 2.1.3 on 2018-11-28 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_auto_20181128_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactionlog',
            old_name='date',
            new_name='datetime',
        ),
    ]
