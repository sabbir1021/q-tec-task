# Generated by Django 4.1 on 2023-06-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='okkk.jpg', upload_to='products'),
            preserve_default=False,
        ),
    ]
