<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class LogAction extends Model
{
    use HasFactory;

    protected $fillable = ['SIMCODE_ID', 'action_id', 'status', 'request', 'direction', 'count_resp'];
}
