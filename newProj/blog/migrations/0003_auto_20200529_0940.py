# Generated by Django 3.0.6 on 2020-05-29 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200529_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='downVote',
            field=models.IntegerField(null=True),
        ),
    ]