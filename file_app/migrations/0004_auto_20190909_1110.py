# Generated by Django 2.2.4 on 2019-09-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0003_auto_20190909_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='file_name',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
