<?php

namespace App\Exceptions;

use Exception;

class CsrfException extends Exception
{
    /**
     * Cria uma nova instância da exceção.
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct("CSRF Token Mismatch");
    }
}
