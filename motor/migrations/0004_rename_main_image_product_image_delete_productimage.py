# Generated by Django 4.1.3 on 2024-11-12 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("motor", "0003_rename_image_product_main_image_productimage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="main_image",
            new_name="image",
        ),
        migrations.DeleteModel(
            name="ProductImage",
        ),
    ]
