# Generated by Django 3.0.3 on 2020-05-10 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edclg', '0009_pdfstore'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfstore',
            name='unid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='edclg.Courseupdate'),
        ),
    ]
