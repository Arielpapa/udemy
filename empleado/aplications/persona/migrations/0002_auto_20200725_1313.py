# Generated by Django 3.0.8 on 2020-07-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidades', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['last_name'], 'verbose_name': 'Mi personal', 'verbose_name_plural': 'Area personal de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'last_name')},
        ),
    ]
