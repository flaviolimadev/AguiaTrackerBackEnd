<?php

namespace App\Http\Controllers;

use App\Models\Header;
use Illuminate\Http\Request;

class HeaderController extends Controller
{
    // Get all headers
    public function index()
    {
        return response()->json(Header::all(), 200);
    }

    // Get a single header by ID
    public function show($id)
    {
        $header = Header::find($id);

        if (!$header) {
            return response()->json(['message' => 'Header not found'], 404);
        }

        return response()->json($header, 200);
    }

    // Create a new header
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'SIMCODE' => 'required|string',
            'headers' => 'nullable|string',
        ]);

        $header = Header::create($validatedData);

        return response()->json($header, 201);
    }

    // Update an existing header
    public function update(Request $request, $id)
    {
        $header = Header::find($id);

        if (!$header) {
            return response()->json(['message' => 'Header not found'], 404);
        }

        $validatedData = $request->validate([
            'SIMCODE' => 'sometimes|required|string',
            'headers' => 'nullable|string',
        ]);

        $header->update($validatedData);

        return response()->json($header, 200);
    }

    // Delete a header
    public function destroy($id)
    {
        $header = Header::find($id);

        if (!$header) {
            return response()->json(['message' => 'Header not found'], 404);
        }

        $header->delete();

        return response()->json(['message' => 'Header deleted successfully'], 200);
    }
}
