# Generated by Django 5.1 on 2024-09-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='vendor',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]