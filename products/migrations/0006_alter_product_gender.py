# Generated by Django 5.0.6 on 2024-06-21 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('U', 'Unisex'), ('M', 'Men'), ('W', 'Women')], max_length=1),
        ),
    ]
