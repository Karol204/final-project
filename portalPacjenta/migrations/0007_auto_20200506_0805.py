# Generated by Django 3.0.6 on 2020-05-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalPacjenta', '0006_auto_20200505_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='placówka',
            name='address',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='placówka',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='placówka',
            name='kontakt',
            field=models.IntegerField(null=True),
        ),
    ]
