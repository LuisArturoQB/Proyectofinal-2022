# Generated by Django 4.0.4 on 2022-10-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapatos',
            name='imagen',
            field=models.ImageField(upload_to='zapatos'),
        ),
    ]
