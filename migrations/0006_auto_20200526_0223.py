# Generated by Django 3.1 on 2020-05-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risapp', '0005_auto_20200525_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
