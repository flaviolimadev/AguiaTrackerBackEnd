<?php

namespace App\Http\Controllers;

use App\Models\Action;
use Illuminate\Http\Request;

class ActionController extends Controller
{
    // Get all actions
    public function index()
    {
        return response()->json(Action::all(), 200);
    }

    // Get a single action by ID
    public function show($id)
    {
        $action = Action::find($id);

        if (!$action) {
            return response()->json(['message' => 'Action not found'], 404);
        }

        return response()->json($action, 200);
    }

    // Create a new action
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'code_status' => 'required|integer',
            'description' => 'nullable|string',
        ]);

        $action = Action::create($validatedData);

        return response()->json($action, 201);
    }

    // Update an existing action
    public function update(Request $request, $id)
    {
        $action = Action::find($id);

        if (!$action) {
            return response()->json(['message' => 'Action not found'], 404);
        }

        $validatedData = $request->validate([
            'code_status' => 'sometimes|required|integer',
            'description' => 'nullable|string',
        ]);

        $action->update($validatedData);

        return response()->json($action, 200);
    }

    // Delete an action
    public function destroy($id)
    {
        $action = Action::find($id);

        if (!$action) {
            return response()->json(['message' => 'Action not found'], 404);
        }

        $action->delete();

        return response()->json(['message' => 'Action deleted successfully'], 200);
    }
}
