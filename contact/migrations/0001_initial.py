# Generated by Django 4.0.1 on 2022-01-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('useremail', models.EmailField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
