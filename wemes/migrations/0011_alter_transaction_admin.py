# Generated by Django 4.0.6 on 2022-07-29 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wemes', '0010_alter_item_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wemes.user'),
        ),
    ]
