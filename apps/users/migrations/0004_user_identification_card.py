# Generated by Django 3.2.7 on 2021-10-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211008_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identification_card',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]