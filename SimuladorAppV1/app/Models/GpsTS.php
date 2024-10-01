<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class GpsTS extends Model
{
    use HasFactory;

    protected $fillable = ['SIMCODE', 'cod_detec', 'status'];
}
