# Generated by Django 4.1.3 on 2024-11-13 13:16

from django.db import migrations, models
import django.db.models.deletion

def assign_default_cart(apps, schema_editor):
    # Get models using the historical version to avoid dependency issues
    Cart = apps.get_model('motor', 'Cart')
    CartItem = apps.get_model('motor', 'CartItem')

    # Create a default cart for any CartItem without a cart
    default_cart = Cart.objects.create()

    # Assign the default cart to all CartItems with a NULL cart
    CartItem.objects.filter(cart__isnull=True).update(cart=default_cart)

class Migration(migrations.Migration):

    dependencies = [
        ("motor", "0007_remove_cartitem_cart_alter_cart_items"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="items",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="motor.cart",
            ),
        ),
        # RunPython to assign a default cart to all CartItems with NULL in cart field
        migrations.RunPython(assign_default_cart),

        # Change cart field to be non-nullable after assigning default cart
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="motor.cart",
            ),
        ),
    ]
