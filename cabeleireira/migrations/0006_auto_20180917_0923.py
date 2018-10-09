# Generated by Django 2.1.1 on 2018-09-17 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Servico', '0004_auto_20180916_1330'),
        ('cabeleireira', '0005_auto_20180917_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabeleireira_Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabeleireira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabeleireira.Cabeleireira')),
                ('servico', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Servico.Servico')),
            ],
        ),
        migrations.RemoveField(
            model_name='cabeleireiraservico',
            name='cabeleireira',
        ),
        migrations.RemoveField(
            model_name='cabeleireiraservico',
            name='servico',
        ),
        migrations.DeleteModel(
            name='CabeleireiraServico',
        ),
    ]