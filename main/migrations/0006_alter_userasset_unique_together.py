# Generated by Django 3.2.23 on 2024-01-19 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_userasset_asset'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userasset',
            unique_together={('portfolio', 'asset')},
        ),
    ]
