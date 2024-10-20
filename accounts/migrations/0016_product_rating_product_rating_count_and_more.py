# Generated by Django 5.1.2 on 2024-10-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_product_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rating_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='slogan',
            field=models.TextField(max_length=100),
        ),
    ]
