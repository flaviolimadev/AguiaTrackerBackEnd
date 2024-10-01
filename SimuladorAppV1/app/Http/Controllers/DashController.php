<?php

namespace App\Http\Controllers;

use App\Models\ActionData;
use App\Models\GpsTS;
use App\Models\Header;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class DashController extends Controller
{
    //
    public function index(){

        return view('_dashboard.home', [
            'auth' =>  Auth::user(),
            'headers' => Header::all(),
            'logAction' => ActionData::all(),
            'Gpss' => GpsTS::where('status', 1)->paginate(1000),
        ]);
    }

    public function arbitrations(){

        return view('_dashboard.arbitration', [
            'auth' =>  Auth::user(),
            'Gpss' => GpsTS::where('status', 1)->paginate(1000),
            'headers' => Header::all()->take(100),
        ]);
    }

    public function automaticBot(){

        return view('_dashboard.automaticbot', [
            'auth' =>  Auth::user(),
        ]);
    }

    public function brokers(){

        return view('_dashboard.brokers', [
            'auth' =>  Auth::user(),
        ]);
    }

    public function tokensAndCrypts(){

        return view('_dashboard.tokensandcrypts', [
            'auth' =>  Auth::user(),
        ]);
    }

    public function reports(){

        return view('_dashboard.reports', [
            'auth' =>  Auth::user(),
        ]);
    }

    public function faqs(){

        return view('_dashboard.home', [
            'auth' =>  Auth::user(),
        ]);
    }

    public function monitorados(){
        return view('_dashboard.monitorados', [
            'auth' =>  Auth::user(),
        ]);
    }

    public function monitorado($id){
        return view('_dashboard.monitorado', [
            'auth' =>  Auth::user(),
        ]);
    }

    public function cadMonitorado(){
        return view('_dashboard.cadMonitorado', [
            'auth' =>  Auth::user(),
        ]);
    }

    
}
