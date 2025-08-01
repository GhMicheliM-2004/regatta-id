# Generated by Django 5.2.4 on 2025-07-21 16:53

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('perfil', models.CharField(choices=[('aluno', 'Aluno'), ('colaborador', 'Colaborador'), ('visitante', 'Visitante'), ('voluntario', 'Voluntário')], max_length=20)),
                ('foto', models.BinaryField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('consentimento_lgpd', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_entrada', models.TimeField()),
                ('hora_saida', models.TimeField()),
                ('dias_semana', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('turma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horarios', to='regatta_id_app.turma')),
            ],
        ),
        migrations.CreateModel(
            name='TentativaAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucesso', models.BooleanField()),
                ('ip_origem', models.CharField(blank=True, max_length=100, null=True)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('motivo', models.TextField(blank=True, null=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tentativas_acesso', to='regatta_id_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='RotaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(max_length=255)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rotas', to='regatta_id_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(max_length=255)),
                ('data_presenca', models.DateField()),
                ('presente', models.BooleanField(default=True)),
                ('turma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='presencas', to='regatta_id_app.turma')),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='presencas', to='regatta_id_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='EventoCritico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_evento', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos_criticos', to='regatta_id_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DadosBiometricos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facial_hash', models.TextField()),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biometrias', to='regatta_id_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AlunoTurma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='regatta_id_app.turma')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turmas_aluno', to='regatta_id_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AcessoRegistrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_acesso', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída')], max_length=20)),
                ('local', models.CharField(max_length=255)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('valido', models.BooleanField(default=True)),
                ('alerta', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acessos_registrados', to='regatta_id_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_acesso', models.CharField(choices=[('admin', 'Admin')], max_length=20)),
                ('autorizado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acessos', to='regatta_id_app.usuario')),
            ],
        ),
    ]
