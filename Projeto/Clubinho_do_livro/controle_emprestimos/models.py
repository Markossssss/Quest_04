from django.db import models

class Colecao(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Colecão'
        verbose_name_plural = 'Coleções'

class Revista(models.Model):
    numero_edicao = models.IntegerField('Número da edição')
    ano = models.IntegerField('Ano de lançamento')
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE, verbose_name='Coleção')

    def __str__(self):
        num = self.numero_edicao
        return str(num)

class Caixa(models.Model):
    numero = models.IntegerField('Número')
    etiqueta = models.CharField('Etiqueta', max_length=50)
    cor = models.CharField('Cor', max_length=20)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)

    def __str__(self):
        num = self.numero
        return str(num)

class Amigo(models.Model):
    nome = models.CharField('Amigo', max_length=50)
    nome_mae = models.CharField('Nome da mãe', max_length=50)
    telefone = models.CharField('Telefone', max_length=13)
    opcoes = [
        ('Prédio', 'Prédio'),
        ('Escola', 'Escola'),
        ]
    grupo_amigo = models.CharField('Grupo do amigo', max_length=100, choices=opcoes, default='')

    def __str__(self):
        return self.nome
class Emprestimo(models.Model):

    data_emprestimo = models.DateField('Data de emprestimo')
    data_devolucao = models.DateField('Data de devolução')
    amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)


# Create your models here.
