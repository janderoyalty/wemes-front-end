# Generated by Django 4.0.6 on 2022-08-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wemes', '0014_alter_transaction_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.ImageField(blank=True, upload_to='code'),
        ),
    ]
