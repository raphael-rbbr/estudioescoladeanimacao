# Generated by Django 4.2.19 on 2025-02-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaings', '0002_remove_inscription_slug_inscription_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='knowloge',
            field=models.CharField(default='outros', help_text='Clique para selecionar', max_length=80, verbose_name='conhecia'),
        ),
    ]
