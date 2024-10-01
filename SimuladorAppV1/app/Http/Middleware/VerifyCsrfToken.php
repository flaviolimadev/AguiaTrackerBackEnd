<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;

class VerifyCsrfToken extends Middleware
{
    /**
     * Os URIs que devem ser ignorados pela verificação CSRF.
     *
     * @var array<int, string>
     */
    protected $except = [
        '/liberar-csrf', // Adiciona a rota específica para ignorar CSRF
    ];
}
