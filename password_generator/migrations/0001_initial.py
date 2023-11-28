# Generated by Django 4.1.13 on 2023-11-26 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='pappu', max_length=45, null=True)),
                ('check_in', models.DateTimeField(blank=True, default=None, null=True)),
                ('check_out', models.DateTimeField(blank=True, default=None, null=True)),
                ('Adults', models.IntegerField(default=11, null=True)),
                ('children', models.IntegerField(default=111, null=True)),
                ('phone_no', models.BigIntegerField(default=98234556677, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='kal', max_length=300, null=True)),
                ('email', models.EmailField(default='kalpitmathur3@gmail.com', max_length=300, null=True)),
                ('message', models.CharField(default='kfek', max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='harshagarwal', max_length=400, null=True)),
                ('last_name', models.CharField(default='harsh', max_length=400, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
