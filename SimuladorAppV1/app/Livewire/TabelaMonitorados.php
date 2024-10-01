<?php

namespace App\Livewire;

use App\Models\GpsTS;
use App\Models\Monitorados;
use Livewire\Component;
use Livewire\WithPagination;

class TabelaMonitorados extends Component
{
    use WithPagination;
    
    public $search = ''; // Propriedade que armazenará o valor da pesquisa

    protected $paginationTheme = 'bootstrap'; // Usa o estilo de paginação do Bootstrap

    public function submitSearch()
    {
        // Sempre que o campo de pesquisa for atualizado, volta para a página 1
        $this->render();
    }

    public function render()
    {
        // Paginar os dados do GPS, 10 itens por página
        // Busca registros no banco de dados filtrando com base na pesquisa
        if($this->search){
            $Gpss = Monitorados::where('name', $this->search)
                        ->paginate(10);
        }else{
            $Gpss = Monitorados::paginate(10);
        }

        return view('livewire.tabela-monitorados', ['Gpss' => $Gpss]);
    }
}