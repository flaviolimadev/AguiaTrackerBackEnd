<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ActionData extends Model
{
    use HasFactory;

    protected $fillable = ['SIMCODE_ID', 'action_id', 'status'];
}
