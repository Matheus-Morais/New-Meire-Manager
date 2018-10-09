# Generated by Django 2.1.1 on 2018-09-17 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Servico', '0004_auto_20180916_1330'),
        ('cabeleireira', '0004_auto_20180917_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabeleireiraServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabeleireira', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cabeleireira.Cabeleireira')),
                ('servico', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Servico.Servico')),
            ],
        ),
        migrations.RemoveField(
            model_name='servico_cabeleireira',
            name='cabeleireira',
        ),
        migrations.RemoveField(
            model_name='servico_cabeleireira',
            name='servico',
        ),
        migrations.DeleteModel(
            name='Servico_Cabeleireira',
        ),
    ]