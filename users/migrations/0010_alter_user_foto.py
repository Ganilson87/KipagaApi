# Generated by Django 4.1.5 on 2023-02-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_provincia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(upload_to='static/images', verbose_name=''),
        ),
    ]
