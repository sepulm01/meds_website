# Generated by Django 2.2.12 on 2020-06-22 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0002_auto_20200622_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='alergias',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicamentos',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patologias',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prevision',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
        ),
    ]