# Generated by Django 2.0 on 2021-01-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_company_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Курс')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Студент')),
                ('courses', models.ManyToManyField(to='apps.Course')),
            ],
        ),
    ]
