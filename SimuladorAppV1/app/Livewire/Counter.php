<?php
 
namespace App\Livewire;
use Livewire\Attributes\On; 
 
use Livewire\Component;
 
class Counter extends Component
{
    public function save()
    {
        // ...
 
        $this->dispatch('post-created'); 
    }

 
    #[On('post-updated.1')] 
    public function refreshPost()
    {
        // ...
    }
 
    
}
