# Generated by Django 4.1.7 on 2023-03-06 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='libid',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, related_name='visitors', to='hello.library'),
        ),
    ]