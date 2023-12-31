# Generated by Django 4.2.4 on 2023-08-18 22:39

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/', verbose_name='Image')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterField(
            model_name='productsize',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ManyToManyField(related_name='products', to='reviews.imagemodel'),
        ),
    ]
