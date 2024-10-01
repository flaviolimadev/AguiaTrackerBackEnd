<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\User;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;

class AuthController extends Controller
{
    //
    public function login(){
        return view('_auth.login');
    }

     // Processar o login
     public function loginPost(Request $request)
     {
         // Validar os campos do formulário
         $request->validate([
             'login' => 'required|string',
             'password' => 'required|string',
         ]);
 
         // Determinar se o campo de login é um email ou nome de usuário
         $loginType = filter_var($request->input('login'), FILTER_VALIDATE_EMAIL) ? 'email' : 'user';
 
         // Tentativa de autenticar o usuário
         $credentials = [
             $loginType => $request->input('login'),
             'password' => $request->input('password'),
         ];
 
         if (Auth::attempt($credentials)) {

             // Cria a sessão 'modotheme' com o valor padrão 'light'
             session(['modotheme' => 'light']);
             
             // Redirecionar para o dashboard ou para onde preferir após o login bem-sucedido
             return redirect()->route('home');
         }
 
         // Retornar com erro caso as credenciais sejam inválidas
         return back()->withErrors([
             'login' => 'The information provided is incorrect.',
         ]);
     }

    public function register(){
        return view('_auth.register');
    }

    // Processar o registro
    public function registerPost(Request $request)
    {
        // Validação dos campos
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'user' => 'required|string|max:255|unique:users',
            'contato' => 'required|string|max:15|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        // Criação do usuário
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'user' => $request->user,
            'contato' => $request->contato,
            'password' => Hash::make($request->password),
        ]);

        // Logar o usuário automaticamente após o registro
        auth()->login($user);

        // Redirecionar para o dashboard ou qualquer outra página
        return redirect()->route('home');
    }

    public function recover(){
        return view('_auth.recover');
    }

    public function logout()
    {
        Auth::logout();
        return redirect('/login');
    }
}

