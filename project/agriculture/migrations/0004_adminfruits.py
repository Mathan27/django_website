# Generated by Django 3.1.2 on 2020-10-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriculture', '0003_auto_20201009_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminfruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='newfolder')),
                ('desc', models.TextField()),
            ],
        ),
    ]
