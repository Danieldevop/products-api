# Generated by Django 2.1.4 on 2018-12-06 16:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181206_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('aeb60d25-93a4-4689-817f-af069b7dd07e'), editable=False),
        ),
    ]
