# Generated by Django 3.2.19 on 2023-05-29 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='SubCategory',
            new_name='sub_category',
        ),
    ]
