# Generated by Django 2.2.7 on 2019-11-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Animal', max_length=50)),
                ('species', models.CharField(help_text='Species of Animal', max_length=100)),
                ('birth_date', models.DateField(help_text='Birth Date')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', help_text='Sex of the pet', max_length=35)),
            ],
        ),
    ]