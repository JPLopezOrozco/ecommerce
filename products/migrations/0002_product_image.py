# Generated by Django 5.0.6 on 2024-06-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='none', upload_to='products/'),
            preserve_default=False,
        ),
    ]
