# Generated by Django 2.2 on 2019-07-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_form', '0002_auto_20190710_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='id',
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='姓名'),
        ),
    ]
