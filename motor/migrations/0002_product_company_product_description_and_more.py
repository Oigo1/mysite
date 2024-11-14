# Generated by Django 4.1.3 on 2024-11-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("motor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="company",
            field=models.CharField(default="Default Company", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(default="No description provided"),
        ),
        migrations.AddField(
            model_name="product",
            name="discount_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=8, null=True
            ),
        ),
    ]
