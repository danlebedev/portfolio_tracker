# Generated by Django 3.2.23 on 2024-01-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_userasset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userasset',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.asset'),
        ),
    ]
