# Generated by Django 5.2.1 on 2025-05-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
        migrations.AddField(
            model_name='quiz',
            name='category_id_external',
            field=models.IntegerField(blank=True, help_text='ID de la Categoría desde el servicio externo', null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='tag_ids_external',
            field=models.CharField(blank=True, default='', help_text='Lista de IDs de Etiquetas (separados por comas) desde el servicio externo', max_length=500),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
