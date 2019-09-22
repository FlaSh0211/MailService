# Generated by Django 2.1.8 on 2019-09-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('emails', models.CharField(max_length=100)),
            ],
        ),
    ]
