# Generated by Django 2.0.5 on 2018-05-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('identificacion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]