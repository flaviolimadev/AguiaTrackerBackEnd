<?php

namespace App\Http\Controllers;

use App\Models\LogAction;
use Illuminate\Http\Request;

class LogActionController extends Controller
{
    // Get all log actions
    public function index()
    {
        return response()->json(LogAction::all(), 200);
    }

    // Get a single log action by ID
    public function show($id)
    {
        $logAction = LogAction::find($id);

        if (!$logAction) {
            return response()->json(['message' => 'LogAction not found'], 404);
        }

        return response()->json($logAction, 200);
    }

    // Create a new log action
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'SIMCODE_ID' => 'required|string',
            'action_id' => 'required|string',
            'status' => 'integer|nullable',
            'request' => 'required|string',
            'direction' => 'integer|nullable',
            'count_resp' => 'integer|nullable',
        ]);

        $logAction = LogAction::create($validatedData);

        return response()->json($logAction, 201);
    }

    // Update an existing log action
    public function update(Request $request, $id)
    {
        $logAction = LogAction::find($id);

        if (!$logAction) {
            return response()->json(['message' => 'LogAction not found'], 404);
        }

        $validatedData = $request->validate([
            'SIMCODE_ID' => 'sometimes|required|string',
            'action_id' => 'sometimes|required|string',
            'status' => 'integer|nullable',
            'request' => 'sometimes|required|string',
            'direction' => 'integer|nullable',
            'count_resp' => 'integer|nullable',
        ]);

        $logAction->update($validatedData);

        return response()->json($logAction, 200);
    }

    // Delete a log action
    public function destroy($id)
    {
        $logAction = LogAction::find($id);

        if (!$logAction) {
            return response()->json(['message' => 'LogAction not found'], 404);
        }

        $logAction->delete();

        return response()->json(['message' => 'LogAction deleted successfully'], 200);
    }
}
