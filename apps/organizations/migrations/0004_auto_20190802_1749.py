# Generated by Django 2.2 on 2019-08-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20190802_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='jg', max_length=2),
        ),
    ]
