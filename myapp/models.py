from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'  # Define explicitamente o nome da tabela
    

    def __str__(self):
        return self.name

class Cache(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    expiration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.key


class Job(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.IntegerField(default=0)
    reserved_at = models.DateTimeField(null=True, blank=True)
    available_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Job {self.id} in queue {self.queue}'

class Monitorado(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Dispositivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    monitorado = models.ForeignKey('Monitorado', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tipo} - {self.modelo}'


class Foto(models.Model):
    id = models.BigAutoField(primary_key=True)
    monitorado = models.ForeignKey('Monitorado', on_delete=models.CASCADE)
    caminho = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Foto de {self.monitorado.nome}'


class Arquivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    caminho = models.CharField(max_length=255)
    tamanho = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero = models.CharField(max_length=15, unique=True)
    monitorado = models.ForeignKey('Monitorado', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numero


class Processo(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero_processo = models.CharField(max_length=50, unique=True)
    monitorado = models.ForeignKey('Monitorado', on_delete=models.CASCADE)
    descricao = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numero_processo


class Estabelecimento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    tipo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f'Perfil de {self.usuario.name}'


class RegraCumprimentoPena(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Regra {self.id} - {self.status}'


class Faccao(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    data_fundacao = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class SituacaoTrabalhista(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.TextField()
    monitorado = models.ForeignKey('Monitorado', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Situação de {self.monitorado.nome}'


class Zona(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class TrackingData(models.Model):
    id = models.BigAutoField(primary_key=True)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE)
    localizacao = models.CharField(max_length=255)
    data_registro = models.DateTimeField()

    def __str__(self):
        return f'Tracking de {self.dispositivo.tipo} em {self.data_registro}'