# Generated by Django 3.2.7 on 2021-09-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parenting', '0006_auto_20210902_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
