# Generated by Django 4.2.3 on 2023-08-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogtitle', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('files', models.FileField(upload_to='files')),
            ],
        ),
    ]
