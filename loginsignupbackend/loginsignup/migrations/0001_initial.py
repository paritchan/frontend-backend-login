# Generated by Django 5.0.3 on 2024-03-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginsignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('dlnum', models.CharField(max_length=50)),
                ('permitnum', models.CharField(max_length=50)),
            ],
        ),
    ]
