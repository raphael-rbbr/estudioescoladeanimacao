# Generated by Django 4.2.19 on 2025-02-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaings', '0006_alter_inscription_dedication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='age',
            field=models.CharField(default=' ', help_text='Clique para selecionar', max_length=50, verbose_name='idade'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='gender',
            field=models.CharField(default=' ', help_text='Clique para selecionar', max_length=50, verbose_name='genero'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='portifolio',
            field=models.TextField(default=' ', help_text='VOCÊ POSSUI UM LOCAL ONDE DIVULGA SEU TRABALHO ARTÍSTICO? EM CASO AFIRMATIVO COMPARTILHE O LINK COM A GENTE!', max_length=80, verbose_name='portifolio'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='studing',
            field=models.CharField(default=' ', help_text='SE ESTIVER ESTUDANDO NESTE ANO, INFORME SÉRIE / PERÍODO:', max_length=50, verbose_name='período'),
        ),
    ]
