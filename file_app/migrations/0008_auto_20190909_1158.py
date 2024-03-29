# Generated by Django 2.2.4 on 2019-09-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0007_filedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='avg_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='avg_max_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='avg_min_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='max_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='max_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='mean_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='min_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='min_temp',
            field=models.IntegerField(default=0),
        ),
    ]
