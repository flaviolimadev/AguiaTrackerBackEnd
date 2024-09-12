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
    key_monitorado = models.CharField(max_length=255)
    matricula_monitorado = models.CharField(max_length=255)
    nome_monitorado = models.CharField(max_length=255)
    dispositivo = models.CharField(max_length=255)
    agencia_id = models.IntegerField()
    estabelecimento_prisional_id = models.IntegerField(default=0)
    monitorado_vitima = models.IntegerField(default=0)
    perfil_id = models.IntegerField()
    nome_completo = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, null=True, blank=True)
    apelido = models.CharField(max_length=255, null=True, blank=True)
    nome_mae = models.CharField(max_length=255)
    nome_pai = models.CharField(max_length=255, null=True, blank=True)
    genero = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField()
    protocolo_monitoramento = models.CharField(max_length=255)
    regime_id = models.IntegerField(default=0)
    controle_prazo = models.CharField(max_length=255, default='0')
    inicio_medida = models.DateField()
    dias_medida = models.IntegerField()
    prorrogacao = models.IntegerField(null=True, blank=True)
    tipo_monitorado_id = models.IntegerField(default=0)
    periculosidade = models.IntegerField(default=0)
    faccao_id = models.IntegerField(null=True, blank=True)
    religiao = models.CharField(max_length=255, null=True, blank=True)
    estado_civil = models.CharField(max_length=255, null=True, blank=True)
    situacao_trabalhista_id = models.IntegerField(default=0)
    escolaridade_id = models.IntegerField(default=0)
    fotos = models.TextField(null=True, blank=True)
    arquivos = models.TextField(null=True, blank=True)
    telefones = models.TextField(null=True, blank=True)
    zonas = models.TextField(null=True, blank=True)
    processos = models.TextField(null=True, blank=True)
    agendamento_servicos = models.TextField(null=True, blank=True)
    comandos_dispositivo = models.TextField(null=True, blank=True)
    notificacoes_observacoes = models.TextField(null=True, blank=True)
    historico_posicoes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'monitorados'  # Define explicitamente o nome da tabela

    def __str__(self):
        return self.nome

class Dispositivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    num_serie = models.CharField(max_length=255)
    versao_firmware = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    sim_card_01 = models.CharField(max_length=255)
    sim_card_02 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dispositivos'

    def __str__(self):
        return f'{self.tipo} - {self.modelo}'


class Foto(models.Model):
    id = models.BigAutoField(primary_key=True)
    foto = models.TextField()  # Armazena longtext
    principal = models.IntegerField(default=0)  # Indica se é a foto principal
    operador_registro = models.IntegerField(default=0)  # ID do operador que registrou
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fotos'

    def __str__(self):
        return f'Foto de {self.monitorado.nome}'


class Arquivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_arquivo = models.CharField(max_length=255)
    formato_arquivo = models.CharField(max_length=255)
    arquivo = models.TextField()  # Armazena o arquivo em formato de texto longo
    operador_registro = models.IntegerField(default=0)  # ID do operador que registrou
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'arquivos'

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero = models.CharField(max_length=255)
    whatsapp = models.IntegerField(default=0)  # Indica se o número é WhatsApp
    tipo_contato = models.CharField(max_length=255)  # Tipo de contato, ex: pessoal, trabalho
    operador_registro = models.IntegerField(default=0)  # ID do operador que registrou
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'telefones'

    def __str__(self):
        return self.id


class Processo(models.Model):
    id = models.BigAutoField(primary_key=True)
    num_processo = models.IntegerField(default=0)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    vara = models.IntegerField()
    magistrado = models.CharField(max_length=255, null=True, blank=True)
    resumo_sentenca = models.CharField(max_length=255, null=True, blank=True)
    ativo = models.IntegerField(default=0)
    principal = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'processos'

    def __str__(self):
        return self.numero_processo


class Estabelecimento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_do_estabelecimento = models.CharField(max_length=255)
    local_do_estabelecimento_prisional = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'estabelecimentos'

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_de_perfil = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'perfils'

    def __str__(self):
        return f'Perfil de {self.usuario.name}'


class RegraCumprimentoPena(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_regime = models.TextField()  # Armazena longtext para o tipo de regime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'regras_cumprimento_penas'

    def __str__(self):
        return f'Regra {self.id} - {self.status}'


class Faccao(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_faccao = models.CharField(max_length=255)
    local_faccao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'faccaos'

    def __str__(self):
        return self.nome


class SituacaoTrabalhista(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_empresa = models.CharField(max_length=255)
    cargo_empresa = models.CharField(max_length=255)
    inicio_da_jornada_trabalho = models.DateTimeField()
    termino_da_jornada_trabalho = models.DateTimeField()
    inicio_do_contrato_trabalho = models.DateTimeField()
    termino_do_contrato_trabalho = models.DateTimeField()
    contato_empresa = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'situação_trabalhistas'

    def __str__(self):
        return f'Situação de {self.monitorado.nome}'


class Zona(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_zona = models.CharField(max_length=255)
    regras_zona = models.CharField(max_length=255)
    endereco_zona = models.CharField(max_length=255)
    observacoes = models.CharField(max_length=255)
    vigencia_inicial_da_zona = models.DateTimeField()
    vigencia_final_da_zona = models.DateTimeField(null=True, blank=True)
    tipo_area = models.CharField(max_length=255)
    regras_horario = models.CharField(max_length=255, null=True, blank=True)
    operador_registro = models.CharField(max_length=255)
    operador_edit_registro = models.IntegerField(default=1)
    ativa = models.IntegerField()
    horario_zona = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'zonas'

    def __str__(self):
        return self.nome


class TrackingData(models.Model):
    id = models.BigAutoField(primary_key=True)
    coordenadas_geograficas = models.CharField(max_length=255)
    LBS = models.CharField(max_length=255)
    status_feixe_luz = models.CharField(max_length=255)
    deteccao_de_jamming = models.CharField(max_length=255)
    deteccao_de_violacao_de_caixa = models.CharField(max_length=255)
    altura = models.CharField(max_length=255)
    velocidade = models.CharField(max_length=255)
    VDOP = models.CharField(max_length=255)
    HDOP = models.CharField(max_length=255)
    qualidade_satelite = models.CharField(max_length=255)
    nivel_bateria = models.CharField(max_length=255)
    e_sim_card = models.CharField(max_length=255)
    inercia = models.CharField(max_length=255)
    qualidade_GPRS = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'traking_data'

    def __str__(self):
        return f'Tracking de {self.dispositivo.tipo} em {self.data_registro}'