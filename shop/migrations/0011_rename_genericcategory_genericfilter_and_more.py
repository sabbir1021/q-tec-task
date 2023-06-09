# Generated by Django 4.1 on 2023-06-03 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GenericCategory',
            new_name='GenericFilter',
        ),
        migrations.CreateModel(
            name='GenericFilterValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generic_filter', to='shop.genericfilter')),
            ],
        ),
        migrations.AlterField(
            model_name='productfilter',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.genericfiltervalues'),
        ),
        migrations.DeleteModel(
            name='GenericValues',
        ),
    ]
