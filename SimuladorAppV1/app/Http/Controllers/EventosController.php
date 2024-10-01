<?php

namespace App\Http\Controllers;

use App\Models\LogEventos;
use Illuminate\Http\Request;

class EventosController extends Controller
{
    // Exibir todos os registros
    public function index()
    {
        return response()->json(LogEventos::all(), 200);
    }

    // Exibir um único registro
    public function show($id)
    {
        $LogEventos = LogEventos::find($id);
        if (!$LogEventos) {
            return response()->json(['message' => 'Evento não encontrado'], 404);
        }
        return response()->json($LogEventos, 200);
    }

    // Criar novo registro
    public function store(Request $request)
    {
        $validated = $request->validate([
            'event_id' => 'required|string',
            'gps_id' => 'required|integer',
            'main' => 'required|string',
            'data' => 'required|string',
            'status' => 'required|integer',
        ]);

        $LogEventos = LogEventos::create($validated);

        return response()->json($LogEventos, 201);
    }

    // Atualizar um registro existente
    public function update(Request $request, $id)
    {
        $LogEventos = LogEventos::find($id);

        if (!$LogEventos) {
            return response()->json(['message' => 'Evento não encontrado'], 404);
        }

        $validated = $request->validate([
            'event_id' => 'required|string',
            'gps_id' => 'required|integer',
            'main' => 'required|string',
            'data' => 'required|string',
            'status' => 'required|integer',
        ]);

        $LogEventos->update($validated);

        return response()->json($LogEventos, 200);
    }

    // Excluir um registro
    public function destroy($id)
    {
        $LogEventos = LogEventos::find($id);

        if (!$LogEventos) {
            return response()->json(['message' => 'Evento não encontrado'], 404);
        }

        $LogEventos->delete();

        return response()->json(['message' => 'Evento deletado com sucesso'], 200);
    }

}
