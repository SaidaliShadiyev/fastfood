# Generated by Django 4.0.1 on 2022-02-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_drinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
