# Generated by Django 4.2.3 on 2023-07-11 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccs', '0004_alter_country_name_alter_vaccine_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]