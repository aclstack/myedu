# Generated by Django 2.2 on 2019-07-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='click_num',
            new_name='click_nums',
        ),
        migrations.RenameField(
            model_name='courseorg',
            old_name='fav_num',
            new_name='fav_nums',
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=20, verbose_name='城市名'),
        ),
    ]