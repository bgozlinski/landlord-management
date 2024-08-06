# Generated by Django 5.0.7 on 2024-08-06 01:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flats", "0001_initial"),
        ("tenants", "0004_remove_tenant_flat"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenant",
            name="flat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tenants",
                to="flats.flat",
            ),
        ),
    ]