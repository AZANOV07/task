# Generated by Django 4.2.4 on 2023-08-23 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_images_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.product'),
        ),
    ]