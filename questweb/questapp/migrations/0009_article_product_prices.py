# Generated by Django 4.1.7 on 2023-03-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questapp', '0008_alter_article_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='product_prices',
            field=models.IntegerField(default=None),
        ),
    ]