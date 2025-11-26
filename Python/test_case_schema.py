"""This file defines the schema for test cases used in validating postconditions."""

# test_case_schema = {
#   "$schema": "http://json-schema.org/draft-07/schema#",
#   "title": "Hypothesis Test Strategy Schema",
#   "type": "object",
#   "properties": {
#     "test_cases": {
#       "type": "array",
#       "minItems": 1,
#       "items": {
#         "type": "object",
#         "properties": {
#           "id": { "type": "string" },
#           "description": { "type": "string" },
          
#           # FIX 1: Relaxed Regex (Allows setup code before 'result =')
#           "execution_statement": {
#             "type": "string",
#             "description": "Python code to call the function. MUST use exact argument names from source.",
#             "pattern": ".*result\\s*=\\s*.+"
#           },
          
#           "input_types": {
#             "type": "object",
#             "description": "Keys MUST match the function argument names exactly.",
#             "additionalProperties": { "type": "string" }
#           },
          
#           "input_constraints": {
#             "type": "object",
#             "description": "Keys MUST match the function argument names exactly.",
#             "additionalProperties": {
#                 # FIX 2: 'anyOf' must be the direct parent to allow different types (Object OR Null)
#                 "anyOf": [
#                     # Option A: A Constraint Object
#                     {
#                       "type": "object",
#                       "properties": {
#                         # FIX 3: Allow Strings for special floats (inf/nan)
#                         "min_val": { "anyOf": [{ "type": "number" }, { "type": "string" }] },
#                         "max_val": { "anyOf": [{ "type": "number" }, { "type": "string" }] },
#                         "min_len": { "type": "integer", "minimum": 0 },
#                         "max_len": { "type": "integer", "minimum": 0 },
#                         "sorted": { "type": "boolean" },
#                         "unique": { "type": "boolean" }
#                       },
#                       "additionalProperties": True # Allows custom keys like 'perfect_square'
#                     },
#                     # Option B: Null (For explicitly unconstrained args)
#                     { 
#                         "type": "null" 
#                     }
#                 ]
#             } 
#           },
          
#           "postconditions": {
#             "type": "array",
#             "minItems": 1,
#             "items": {
#               "type": "object",
#               "properties": { "assertion": { "type": "string" } },
#               "required": ["assertion"]
#             }
#           }
#         },
#         "required": ["id", "description", "execution_statement", "input_types", "postconditions"],
#         "additionalProperties": False
#       }
#     }
#   },
#   "required": ["test_cases"],
#   "additionalProperties": False
# }

test_case_schema = {
  "type": "object",
  "properties": {
    "test_cases": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "description": { "type": "string" },
          "execution_statement": { 
              "type": "string", 
              "pattern": ".*\\w+\\s*=\\s*.+"
          },
          "input_types": { 
              "type": "object",
              "additionalProperties": { "type": "string" }
          },
          "input_constraints": { 
              "type": "object",
              # FIX IS HERE: No "type": "object" at this level!
              "additionalProperties": {
                  "anyOf": [
                      { 
                          "type": "object",
                          "properties": {
                            # Numeric Constraints
                            "min_val": { "anyOf": [{ "type": "number" }, { "type": "string" }] },
                            "max_val": { "anyOf": [{ "type": "number" }, { "type": "string" }] },
                            
                            # Container Constraints
                            "min_len": { "type": "integer", "minimum": 0 },
                            "max_len": { "type": "integer", "minimum": 0 },
                            
                            # String Constraints
                            "pattern": { "type": "string" },
                            "max_codepoint": { "type": "integer", "minimum": 0 },
                            
                            "allow_none": { "type": "boolean" },
                            "is_mixed": { "type": "boolean" },
                            "is_hashable_mix": { "type": "boolean" },
                            # Flags
                            "sorted": { 
                                "anyOf": [
                                    { "type": "boolean" }, 
                                    { "type": "string", "enum": ["ascending", "descending"] }
                                ] 
                            },
                            "unique": { "type": "boolean" }
                          },
                          "additionalProperties": True 
                      },
                      { 
                          "type": "null" 
                      },
                  ]
              } 
          },
          # --- ADD THIS NEW FIELD ---
          "assumptions": {
              "type": "array",
              "description": "List of Python boolean expressions. If False, input is discarded.",
              "items": { "type": "string" }
          },
          # --------------------------
          "postconditions": { 
              "type": "array", 
              "items": { 
                  "type": "object", 
                  "required": ["assertion"],
                  "properties": { "assertion": { "type": "string" } } 
              } 
          }
        },
        "required": ["id", "execution_statement", "input_types", "postconditions"]
      }
    }
  },
  "required": ["test_cases"]
}