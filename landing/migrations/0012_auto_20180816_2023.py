# Generated by Django 2.1 on 2018-08-16 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20180812_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('composition', models.CharField(max_length=50, null=True, verbose_name='Состав')),
                ('weight', models.CharField(max_length=50, null=True, verbose_name='Вес, г.')),
                ('price', models.CharField(max_length=50, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='menu',
        ),
        migrations.AlterField(
            model_name='menu',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.Event', verbose_name='Событие'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menus',
            field=models.ManyToManyField(to='landing.Menu'),
        ),
    ]
