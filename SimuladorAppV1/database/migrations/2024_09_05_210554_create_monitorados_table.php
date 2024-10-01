<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('monitorados', function (Blueprint $table) {
            $table->id();
            $table->string('key_monitorado');  // Primary Key Monitorado
            $table->string('matricula_monitorado');  // Matricula Monitorado
            $table->string('nome_monitorado');  // Nome Monitorado
            $table->string('dispositivo');  // Dispositivo
            $table->integer('agencia_id'); // Relacionado com Agência
            $table->integer('estabelecimento_prisional_id')->default(0);  // Relacionado com Estabelecimento Prisional
            $table->integer('monitorado_vitima')->default(0);  // Monitorado/Vítima (boolean)
            $table->integer('perfil_id');  // Relacionado com Perfil
            $table->string('nome_completo');  // Nome completo
            $table->string('nome_social')->nullable();  // Nome social
            $table->string('apelido')->nullable();  // Apelido
            $table->string('nome_mae');  // Nome da Mãe
            $table->string('nome_pai')->nullable();  // Nome do Pai
            $table->string('genero');  // Gênero
            $table->string('cpf', 11);  // CPF
            $table->string('rg')->nullable();  // RG
            $table->date('data_nascimento');  // Data de Nascimento
            $table->string('protocolo_monitoramento');  // Protocolo de Monitoramento
            $table->integer('regime_id')->default(0);  // Relacionado com Regime de cumprimento de pena
            $table->string('controle_prazo')->default(0);  // Controle de Prazo
            $table->date('inicio_medida');  // Início da Medida
            $table->integer('dias_medida');  // Dias da Medida
            $table->integer('prorrogacao')->nullable();  // Prorrogação
            $table->integer('tipo_monitorado_id')->default(0);  // Relacionado com Tipo de Monitorado
            $table->integer('periculosidade')->default(0);  // Periculosidade (boolean)
            $table->integer('faccao_id')->nullable();  // Facção
            $table->string('religiao')->nullable();  // Religião
            $table->string('estado_civil')->nullable();  // Estado Civil
            $table->integer('situacao_trabalhista_id')->default(0);  // Situação Trabalhista
            $table->integer('escolaridade_id')->default(0); // Escolaridade
            $table->longText('fotos')->nullable();  // Fotos (armazenado em JSON)
            $table->longText('arquivos')->nullable();  // Arquivos (armazenado em JSON)
            $table->longText('telefones')->nullable();  // Telefones (armazenado em JSON)
            $table->longText('zonas')->nullable();  // Zonas (armazenado em JSON)
            $table->longText('processos')->nullable();  // Processos (armazenado em JSON)
            $table->longText('agendamento_servicos')->nullable();  // Agendamento de Serviços (armazenado em JSON)
            $table->longText('comandos_dispositivo')->nullable();  // Comandos do dispositivo (armazenado em JSON)
            $table->longText('notificacoes_observacoes')->nullable();  // Notificações e Observações (armazenado em JSON)
            $table->longText('historico_posicoes')->nullable();  // Histórico de Posições (armazenado em JS
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('monitorados');
    }
};
