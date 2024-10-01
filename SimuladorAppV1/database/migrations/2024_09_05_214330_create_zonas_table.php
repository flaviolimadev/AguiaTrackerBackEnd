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
        Schema::create('zonas', function (Blueprint $table) {
            $table->id();
            $table->string('tipo_zona');
            $table->string('regras_zona');
            $table->string('endereco_zona');
            $table->string('observações');
            $table->dateTime('vigencia_inicial_da_zona');
            $table->dateTime('vigencia_final_da_zona')->nullable();
            $table->string('tipo_area');
            $table->string('regras_horario')->nullable();
            $table->string('operador_registro');
            $table->integer('operador_edit_registro')->default();
            $table->integer('ativa');
            $table->dateTime('horario_zona');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('zonas');
    }
};
