# Generated by Django 3.2.7 on 2021-10-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_identification_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='identification_card',
            field=models.FloatField(unique=True),
        ),
    ]