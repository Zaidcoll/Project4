# Generated by Django 2.2.4 on 2019-11-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20191120_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
