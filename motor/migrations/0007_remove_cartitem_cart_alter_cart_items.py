# Generated by Django 4.1.3 on 2024-11-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("motor", "0006_cartitem_cart_alter_cart_items"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="cart",
        ),
        migrations.AlterField(
            model_name="cart",
            name="items",
            field=models.ManyToManyField(to="motor.cartitem"),
        ),
    ]
