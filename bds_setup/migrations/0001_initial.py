# Generated by Django 2.0.3 on 2018-07-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=5)),
                ('area', models.CharField(max_length=5)),
                ('station', models.CharField(max_length=8)),
                ('floor', models.IntegerField(max_length=1)),
            ],
        ),
    ]
