# Generated by Django 2.2 on 2019-06-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_auto_20190613_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='experience',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='education',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='notes',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='skills',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
