# Generated by Django 3.2.7 on 2021-10-10 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condominium', '0002_subarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=255)),
                ('SubArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominium.subarea')),
            ],
            options={
                'verbose_name': 'house',
                'verbose_name_plural': 'houses',
            },
        ),
    ]
