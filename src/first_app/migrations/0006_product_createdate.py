# Generated by Django 2.2.6 on 2019-10-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20191023_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='createdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
