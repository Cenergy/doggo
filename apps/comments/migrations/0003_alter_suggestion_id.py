# Generated by Django 3.2.1 on 2021-05-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_suggestion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]