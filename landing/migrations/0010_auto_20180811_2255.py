# Generated by Django 2.1 on 2018-08-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20180811_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='special',
            field=models.BooleanField(default=False, verbose_name='Специальное предложение'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
