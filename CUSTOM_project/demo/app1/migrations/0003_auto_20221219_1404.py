# Generated by Django 3.2.12 on 2022-12-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20221216_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='custom',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]