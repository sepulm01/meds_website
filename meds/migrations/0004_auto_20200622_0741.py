# Generated by Django 2.2.12 on 2020-06-22 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0003_auto_20200622_0724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alergias',
            options={'verbose_name_plural': 'Alergias'},
        ),
        migrations.AlterModelOptions(
            name='medicamentos',
            options={'verbose_name_plural': 'Medicamentos'},
        ),
        migrations.AlterModelOptions(
            name='prevision',
            options={'verbose_name_plural': 'Previsión Soc.'},
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='calle',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='sange',
        ),
        migrations.AddField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(default=1, max_length=100, verbose_name='direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='sangre',
            field=models.CharField(choices=[('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], default=1, max_length=10, verbose_name='sangre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alergias',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
        ),
        migrations.AlterField(
            model_name='medicamentos',
            name='dosis',
            field=models.CharField(max_length=20, verbose_name='Dosis'),
        ),
        migrations.AlterField(
            model_name='medicamentos',
            name='med_nom',
            field=models.CharField(max_length=20, verbose_name='Medicamento'),
        ),
        migrations.AlterField(
            model_name='medicamentos',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
        ),
        migrations.AlterField(
            model_name='patologias',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
        ),
        migrations.AlterField(
            model_name='prevision',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meds.Paciente'),
        ),
    ]
