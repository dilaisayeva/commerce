# Generated by Django 2.2.6 on 2019-10-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_product_createdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updatedate',
            field=models.CharField(default='ghbj', max_length=50),
        ),
    ]