# Generated by Django 4.1.7 on 2023-03-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ordered_date',
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]