# Generated by Django 4.1.7 on 2023-05-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin status'),
        ),
    ]