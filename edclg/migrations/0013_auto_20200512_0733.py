# Generated by Django 3.0.3 on 2020-05-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edclg', '0012_coursesingleupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unqid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('message', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='coursesingleupdate',
        ),
    ]
