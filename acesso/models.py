from django.db import models
from django.contrib.auth.models import User 

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=256, choices=(('M', 'Masculino'), ('F', 'Feminino')))

    def __str__(self):
        return self.user.username

class Turma(models.Model):
    nome = models.CharField(max_length=256)
    periodo = models.CharField(max_length=256)
    id_professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    titulo = models.CharField(max_length=256)
    descricao = models.TextField()
    id_turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    id_professor = models.OneToOneField(Professor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo
