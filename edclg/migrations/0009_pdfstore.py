# Generated by Django 3.0.3 on 2020-05-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edclg', '0008_delete_pdfstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdfstore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacheremail', models.CharField(max_length=100)),
                ('unqid', models.TextField(max_length=50)),
                ('file', models.FileField(upload_to='media')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
