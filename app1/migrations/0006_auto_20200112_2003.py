# Generated by Django 3.0a1 on 2020-01-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200112_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='fmoney',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='foodpair',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]