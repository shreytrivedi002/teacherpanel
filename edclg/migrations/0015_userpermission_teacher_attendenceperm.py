# Generated by Django 3.0.3 on 2020-05-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edclg', '0014_userpermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpermission',
            name='teacher_attendenceperm',
            field=models.BooleanField(default=False),
        ),
    ]
