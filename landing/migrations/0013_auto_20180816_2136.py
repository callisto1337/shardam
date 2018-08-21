# Generated by Django 2.1 on 2018-08-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_auto_20180816_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('events', models.ManyToManyField(related_name='images', to='landing.Event')),
            ],
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menus',
            field=models.ManyToManyField(related_name='items', to='landing.Menu', verbose_name='Меню'),
        ),
    ]
