# Generated by Django 3.2.1 on 2021-05-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
