# Generated by Django 4.1.13 on 2023-11-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_generator', '0002_alter_book_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='check_in',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='check_out',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
    ]
