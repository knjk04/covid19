# Generated by Django 4.2.3 on 2023-07-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccs', '0003_alter_source_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
