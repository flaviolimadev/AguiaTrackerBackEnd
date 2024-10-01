<?php

namespace App\Http\Controllers;

use App\Models\ActionData;
use Illuminate\Http\Request;

class ActionDataController extends Controller
{
    // Get all action data
    public function index()
    {
        return response()->json(ActionData::all(), 200);
    }

    // Get a single action data by ID
    public function show($id)
    {
        $actionData = ActionData::find($id);

        if (!$actionData) {
            return response()->json(['message' => 'ActionData not found'], 404);
        }

        return response()->json($actionData, 200);
    }

    // Create a new action data
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'SIMCODE_ID' => 'required|string',
            'action_id' => 'required|string',
            'status' => 'integer|nullable',
        ]);

        $actionData = ActionData::create($validatedData);

        return response()->json($actionData, 201);
    }

    // Update an existing action data
    public function update(Request $request, $id)
    {
        $actionData = ActionData::find($id);

        if (!$actionData) {
            return response()->json(['message' => 'ActionData not found'], 404);
        }

        $validatedData = $request->validate([
            'SIMCODE_ID' => 'sometimes|required|string',
            'action_id' => 'sometimes|required|string',
            'status' => 'integer|nullable',
        ]);

        $actionData->update($validatedData);

        return response()->json($actionData, 200);
    }

    // Delete action data
    public function destroy($id)
    {
        $actionData = ActionData::find($id);

        if (!$actionData) {
            return response()->json(['message' => 'ActionData not found'], 404);
        }

        $actionData->delete();

        return response()->json(['message' => 'ActionData deleted successfully'], 200);
    }
}
