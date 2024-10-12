# Generated by Django 5.1 on 2024-09-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft', '0003_customuser_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('days', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]