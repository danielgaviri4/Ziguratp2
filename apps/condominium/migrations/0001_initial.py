# Generated by Django 3.2.8 on 2021-10-08 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('extension', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('stratum', models.IntegerField(default=1)),
                ('state', models.BooleanField(default=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Condominium',
                'verbose_name_plural': 'Condominiums',
            },
        ),
    ]