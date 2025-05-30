# Generated by Django 5.2.1 on 2025-05-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='atividade_principal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='cep',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='email',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='logradouro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
