# Generated by Django 4.0.1 on 2022-03-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_order_orderproduct_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.RemoveField(
            model_name='drinks',
            name='price',
        ),
        migrations.AddField(
            model_name='drinks',
            name='face',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drinks',
            name='inst',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]