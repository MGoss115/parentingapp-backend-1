# Generated by Django 3.2.7 on 2021-09-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parenting', '0004_alter_kid_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='chores',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='todo',
            name='homework',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='todo',
            name='recreational',
            field=models.CharField(max_length=1000),
        ),
    ]
