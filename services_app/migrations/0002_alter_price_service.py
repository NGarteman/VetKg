# Generated by Django 3.2.9 on 2022-01-05 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='services_app.service'),
        ),
    ]
