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
        Schema::create('processos', function (Blueprint $table) {
            $table->id();
            $table->integer('num_processo')->default(0);
            $table->string('estado');
            $table->string('município');
            $table->integer('vara');
            $table->string('magistrado')->nullable();
            $table->string('resumo_sentenca')->nullable();
            $table->integer('ativo')->default(0);
            $table->integer('principal')->default(0);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('processos');
    }
};
