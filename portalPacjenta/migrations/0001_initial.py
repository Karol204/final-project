# Generated by Django 3.0.6 on 2020-05-04 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lekarz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('surname', models.CharField(max_length=24)),
                ('specialization', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pacjent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('surname', models.CharField(max_length=24)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('med_first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalPacjenta.Lekarz')),
            ],
        ),
        migrations.CreateModel(
            name='Placówka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=64)),
                ('doc', models.ManyToManyField(to='portalPacjenta.Lekarz')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalPacjenta.Pacjent')),
            ],
        ),
        migrations.CreateModel(
            name='Konsultacja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalPacjenta.Lekarz')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portalPacjenta.Pacjent')),
            ],
        ),
    ]