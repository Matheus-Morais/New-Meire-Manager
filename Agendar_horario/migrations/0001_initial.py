# Generated by Django 2.1.1 on 2018-09-17 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabeleireira', '0006_auto_20180917_0923'),
        ('Accounts', '0003_auto_20180914_0908'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(unique=True)),
                ('status', models.BooleanField(choices=[('SO', 'Solicitado'), ('CO', 'Confirmado'), ('EA', 'Em Andamento'), ('C', 'Concluido')], default='SO', max_length=2, verbose_name='Status')),
                ('cabeleireira_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabeleireira.Cabeleireira_Servico')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Usuario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
