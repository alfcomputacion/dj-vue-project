# Generated by Django 4.1.7 on 2023-04-19 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='featured',
            field=models.BooleanField(),
        ),
    ]