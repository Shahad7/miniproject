# Generated by Django 4.1.7 on 2023-05-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_book_stock_alter_myuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
