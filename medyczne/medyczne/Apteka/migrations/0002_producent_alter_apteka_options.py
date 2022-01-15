# Generated by Django 4.0.1 on 2022-01-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apteka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Producent',
                'verbose_name_plural': 'Producenci',
            },
        ),
        migrations.AlterModelOptions(
            name='apteka',
            options={'verbose_name': 'Apteka', 'verbose_name_plural': 'Apteki'},
        ),
    ]