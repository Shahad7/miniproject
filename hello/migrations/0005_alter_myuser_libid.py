# Generated by Django 4.1.7 on 2023-03-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_alter_myuser_libid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='libid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
