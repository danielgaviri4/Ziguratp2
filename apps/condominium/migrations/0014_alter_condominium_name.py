# Generated by Django 3.2.7 on 2021-10-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominium', '0013_alter_adminhistory_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominium',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
