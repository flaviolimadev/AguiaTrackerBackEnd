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
        Schema::create('traking_data', function (Blueprint $table) {
            $table->id();
            $table->string('coordenadas_geograficas');
            $table->string('LBS');
            $table->string('status_feixe_luz');
            $table->string('deteccao_de_jamming');
            $table->string('deteccao_de_violacao_de_caixa');
            $table->string('altura');
            $table->string('velocidade');
            $table->string('VDOP');
            $table->string('HDOP');
            $table->string('qualidade_satelite');
            $table->string('nivel_bateria');
            $table->string('e_sim_card');
            $table->string('inercia');
            $table->string('qualidade_GPRS');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('traking_data');
    }
};
