# Generated by Django 4.1.5 on 2023-02-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_endereco1_user_endereco2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default=2, max_length=50),
            preserve_default=False,
        ),
    ]
