<?php

namespace App\Http\Livewire;

use Livewire\Component;
use Livewire\WithPagination;
use App\Models\GpsTS;

class TabelaGPS extends Component
{
    use WithPagination;

    protected $paginationTheme = 'bootstrap'; // Usa o estilo de paginação do Bootstrap

    public function render()
    {
        // Paginar os dados do GPS, 10 itens por página
        $Gpss = GpsTS::paginate(10);

        return view('livewire.tabela-gps', ['Gpss' => $Gpss]);
    }
}

