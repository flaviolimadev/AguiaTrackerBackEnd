<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class LogEventos extends Model
{
    use HasFactory;
    protected $fillable = [
        'event_id',
        'gps_id',
        'main',
        'data',
        'status',
    ];
}
