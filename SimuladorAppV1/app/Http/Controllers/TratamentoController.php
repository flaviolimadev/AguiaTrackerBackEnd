<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth as FacadesAuth;

class TratamentoController extends Controller
{
    //
    public function index(){

        return view('_dashboard.tratamento', [
            'auth' =>  FacadesAuth::user(),
        ]);
    }
}
