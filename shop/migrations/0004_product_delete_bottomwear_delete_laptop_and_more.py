# Generated by Django 5.1.3 on 2025-01-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.DeleteModel(
            name='BottomWear',
        ),
        migrations.DeleteModel(
            name='Laptop',
        ),
        migrations.DeleteModel(
            name='Mobile',
        ),
        migrations.DeleteModel(
            name='TopWear',
        ),
    ]
