<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;
use Closure;

class DisableCsrf
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        // Desabilitar o CSRF apenas para rotas específicas
        app()->forgetMiddleware(\Illuminate\Foundation\Http\Middleware\VerifyCsrfToken::class);
        
        return $next($request);
    }
}
