# Generated by Django 4.2 on 2023-05-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the first name of the doctor', max_length=40, verbose_name='First name')),
                ('lastName', models.CharField(help_text='Enter the last name of the doctor', max_length=45, verbose_name='Last name')),
                ('specialization', models.CharField(blank=True, choices=[('neurology', 'Neurology'), ('orthopedics', 'Orthopedics'), ('pediatrics', 'Pediatrics'), ('cardiology', 'Cardiology'), ('other', 'Other')], help_text='Select Doctor´s specialization', max_length=20, verbose_name='Specialization')),
            ],
            options={
                'verbose_name': 'Doktor',
                'verbose_name_plural': 'Doktoři',
                'ordering': ['lastName', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name of the medicine', max_length=55, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='A description of the medicine', verbose_name='Description')),
            ],
            options={
                'verbose_name': 'lék',
                'verbose_name_plural': 'léky',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the first name of the pacient', max_length=40, verbose_name='First name')),
                ('lastName', models.CharField(help_text='Enter the last name of the pacient', max_length=45, verbose_name='Last name')),
                ('admission', models.DateTimeField(auto_now=True)),
                ('doctors', models.ManyToManyField(to='myapp.doctor')),
                ('medicine', models.ManyToManyField(to='myapp.medicine')),
            ],
            options={
                'verbose_name': 'Pacient',
                'verbose_name_plural': 'Pacienti',
                'ordering': ['admission', 'lastName'],
            },
        ),
    ]