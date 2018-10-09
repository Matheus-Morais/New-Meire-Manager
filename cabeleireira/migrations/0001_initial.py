# Generated by Django 2.1.1 on 2018-09-17 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Servico', '0004_auto_20180916_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabeleireira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('numero', models.CharField(max_length=11, verbose_name='Numero')),
                ('trabalhos_realizados', models.IntegerField(blank=True, default=0, verbose_name='Valor Desconto')),
            ],
        ),
        migrations.CreateModel(
            name='Cabeleireira_Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabeleireira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabeleireira.Cabeleireira')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servico.Servico')),
            ],
        ),
    ]