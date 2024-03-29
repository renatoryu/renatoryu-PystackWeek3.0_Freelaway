# Generated by Django 4.0.3 on 2022-04-06 14:56
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('D', 'Design'), ('EV', 'Edição de Vídeo')], default='D', max_length=2)),
                ('prazo_entrega', models.DateTimeField()),
                ('preco', models.FloatField()),
                ('reservado', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando aprovação'), ('F', 'Finalizado')], default='AA', max_length=2)),
                ('profissional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Referencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='referencias')),
            ],
        ),
        migrations.DeleteModel(
            name='Teste',
        ),
        migrations.AddField(
            model_name='jobs',
            name='referencias',
            field=models.ManyToManyField(to='jobs.referencias'),
        ),
    ]
