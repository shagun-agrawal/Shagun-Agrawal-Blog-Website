# Generated by Django 2.2 on 2021-05-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='photo',
            field=models.ImageField(upload_to='myimage/'),
        ),
    ]
