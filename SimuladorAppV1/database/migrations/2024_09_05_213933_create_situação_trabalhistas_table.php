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
        Schema::create('situação_trabalhistas', function (Blueprint $table) {
            $table->id();
            $table->string('nome_empresa');
            $table->string('cargo_empresa');
            $table->dateTime('nicio_da_jornada_trabalho');
            $table->dateTime('termino_da_jornada_trabalho');
            $table->dateTime('inicio_do_contrato_trabalho');
            $table->dateTime('termino_do_contrato_trabalho');
            $table->string('contato_empresa');
            $table->string('responsavel');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('situação_trabalhistas');
    }
};
