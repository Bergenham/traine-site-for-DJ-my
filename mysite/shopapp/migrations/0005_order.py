# Generated by Django 5.0.3 on 2024-03-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_rename_flout_product_prise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_adres', models.TextField(blank=True, null=False)),
                ('promocod', models.CharField(max_length=20, null=True,blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
