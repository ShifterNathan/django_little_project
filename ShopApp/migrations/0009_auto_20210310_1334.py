# Generated by Django 3.1.6 on 2021-03-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0008_auto_20210310_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ShopApp'),
        ),
    ]
