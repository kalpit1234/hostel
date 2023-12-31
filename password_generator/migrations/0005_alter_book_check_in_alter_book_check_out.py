# Generated by Django 4.1.13 on 2023-11-26 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('password_generator', '0004_alter_book_check_in_alter_book_check_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='check_in',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='check_out',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
