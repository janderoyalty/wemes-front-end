# Generated by Django 4.0.6 on 2022-07-31 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wemes', '0002_item_description_item_follow_up_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_four',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.PositiveBigIntegerField(max_length=10),
        ),
    ]
