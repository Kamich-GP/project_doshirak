# Generated by Django 5.1.5 on 2025-01-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pr_photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
