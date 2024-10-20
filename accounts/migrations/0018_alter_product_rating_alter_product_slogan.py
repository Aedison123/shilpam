# Generated by Django 5.1.2 on 2024-10-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_product_rating_count_alter_product_slogan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='slogan',
            field=models.TextField(max_length=100),
        ),
    ]
