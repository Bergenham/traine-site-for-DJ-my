# Generated by Django 5.1.4 on 2025-01-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True, null=True)),
                ('p_d', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
