# Generated by Django 3.0.3 on 2020-05-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edclg', '0015_userpermission_teacher_attendenceperm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpermission',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]