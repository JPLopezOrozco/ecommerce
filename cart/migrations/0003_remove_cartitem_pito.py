# Generated by Django 5.0.6 on 2024-06-23 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_pito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='pito',
        ),
    ]
