# Generated by Django 4.2 on 2023-05-03 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questapp', '0011_alter_article_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
