# Generated by Django 4.1.5 on 2023-02-07 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nivel',
            field=models.CharField(choices=[('Ceo', 'Ceo'), ('Agente', 'Agente'), ('App', 'App')], default=2, max_length=50),
            preserve_default=False,
        ),
    ]
