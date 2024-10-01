<?php

namespace App\Http\Controllers;

use App\Models\GpsTS;
use Illuminate\Http\Request;

class GpsTSController extends Controller
{
    // Get all GPS TS records
    public function index()
    {
        return response()->json(GpsTS::all(), 200);
    }

    // Get a single GPS TS record by ID
    public function show($id)
    {
        $gpsTS = GpsTS::find($id);

        if (!$gpsTS) {
            return response()->json(['message' => 'GpsTS not found'], 404);
        }

        return response()->json($gpsTS, 200);
    }

    // Create a new GPS TS record
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'SIMCODE' => 'required|string',
            'cod_detec' => 'nullable|string',
            'status' => 'integer|nullable',
        ]);

        $gpsTS = GpsTS::create($validatedData);

        return response()->json($gpsTS, 201);
    }

    // Update an existing GPS TS record
    public function update(Request $request, $id)
    {
        $gpsTS = GpsTS::find($id);

        if (!$gpsTS) {
            return response()->json(['message' => 'GpsTS not found'], 404);
        }

        $validatedData = $request->validate([
            'SIMCODE' => 'sometimes|required|string',
            'cod_detec' => 'nullable|string',
            'status' => 'integer|nullable',
        ]);

        $gpsTS->update($validatedData);

        return response()->json($gpsTS, 200);
    }

    // Delete a GPS TS record
    public function destroy($id)
    {
        $gpsTS = GpsTS::find($id);

        if (!$gpsTS) {
            return response()->json(['message' => 'GpsTS not found'], 404);
        }

        $gpsTS->delete();

        return response()->json(['message' => 'GpsTS deleted successfully'], 200);
    }
}
