# Generated by Django 4.2.4 on 2023-08-18 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_imagemodel_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='image',
        ),
    ]
