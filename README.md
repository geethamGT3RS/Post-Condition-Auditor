# Post-Condition Auditor Pipeline

This project systematically benchmarks and analyzes different LLM prompt strategies for generating post-conditions of programming functions.  
The focus is on **automated software verification**, measuring prompt strategies for **correctness**, **completeness**, and **reliability** using quantitative metrics.

Each function from the **MBPP** dataset is evaluated through a three-track system:

- **Correctness (PBT):** Are the post-conditions valid?  
- **Completeness (Mutation Analysis):** Are the LLM's assert statements strong enough to actually catch bugs?  
- **Soundness (Static Analysis):** Are the post-conditions free of hallucinated variables?

This repository contains the complete pipeline for **data ingestion**, **prompt generation**, **LLM interaction**, and **results auditing**.


---

## 1. Setup and Installation

Follow these steps to set up your local development environment.

### Step 1: Clone the Repository

Clone this project to your local machine:

```
git clone https://github.com/geethamGT3RS/Post-Condition-Auditor.git
cd Post-Condition-Auditor
```

### Step 2: Create a Python Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

**On macOS/Linux:**

```
source venv/bin/activate
```

**On Windows (PowerShell):**

```
.\venv\Scripts\activate
```

(Your terminal prompt will change to show `(venv)` at the beginning.)

### Step 4: Install Dependencies

Install all required Python packages:

```
pip install -r requirements.txt
```

---

## 2. Configuration

This project requires credentials for your **MongoDB database** and the **Gemini API**.  
These are stored securely in a `.env` file.

### Step 1: Create the `.env` File

This repository includes a template named `.env.example`.  
Make a copy and name it `.env`:

**On macOS/Linux:**

```
cp .env.example .env
```

**On Windows:**

```
copy .env.example .env
```

### Step 2: Edit Your `.env` File

Open `.env` in your code editor and add your secret keys.

```
# --- .env ---

# Your MongoDB connection string.
# (This example uses a local database URL — replace if needed)
MONGO_URI="mongodb://localhost:27017/PostconditionsDB"

# Your Google AI Studio (Gemini) API Key
GEMINI_API_KEY="YOUR_API_KEY_GOES_HERE"
```

**Important:** The `.gitignore` file is already configured to ignore `.env` to prevent secret commits.

---

## 3. Execution Pipeline

These scripts must be run **in order**.  
Ensure your virtual environment is active (`source venv/bin/activate`) before execution.

---

### Step 1: Initialize the Database

This script reads `sanitized-mbpp.json` from the `/Data` folder, processes it, and populates the `Functions` collection.

```
python Python/initializeData.py
```

**What it does:** Creates the `Functions` collection in your database (**427 documents**).

---

### Step 2: Generate All Prompts

This script reads each function from the database and generates prompts for each strategy (Naive, ChainOfThought).

```
python Python/generatePrompts.py
```

**What it does:** Creates the `FunctionPrompts` collection (**427 prompts × 2 strategies = 854 documents**).

---

### Step 3: Run LLM Interaction

This script finds all pending prompts and sends them to the Gemini API concurrently.

```
python Python/llm_integration.py
```

**What it does:** Fills empty `Post_Conditions` arrays in the `FunctionPrompts` collection with responses from the LLM.  
*(Takes a long time to complete.)*

---

### Step 4: Run Static Analysis (Hallucination Audit)

This script runs **Track 3: Soundness** — checking for hallucinated variables.

```
python Python/static_analysis.py
```

**What it does:**  
Updates the `Hallucination_Score` to `1.0` (pass) or `0.0` (fail) for each prompt document.

---

## 4. Database Structure

The pipeline uses two main collections in your MongoDB database.

---

### **Functions Collection**

**Populated by:** `InitiliseData.py`  
**Purpose:** Stores the "ground truth" for each programming problem.

**Example Document:**

```
{
  "_id": "...",
  "Function_ID": 7,
  "Function_Description": "Write a function to find all words which are at least 4 characters long in a string.",
  "Function_Code": "import re\ndef find_char_long(text):\n  return (re.findall(r\"\\b\\w{4,}\\b\", text))",
  "Function_Imports": ["import re"],
  "Function_Test_Cases": [
    "assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])"
  ],
  "Function_Prompts": []
}
```

---

### **FunctionPrompts Collection**

**Populated by:** `generatepromts.py`  
**Updated by:** `llm_interaction.py`, `static_analysis.py`  
**Purpose:** Stores each prompt, its generated response, and audit results.

**Example Document (After LLM Interaction):**

```
{
  "_id": "...",
  "Prompt_ID": 14,
  "Function_ID": 7,
  "Prompt_Text": "...(ChainOfThought prompt text)...",
  "Prompt_Strategy": "ChainOfThought_strategy",
  "Post_Conditions": [
    {
      "description": "The function returns a list.",
      "assert_statement": "isinstance(find_char_long('test'), list)"
    },
    {
      "description": "All strings in the returned list have a length of 4 or more.",
      "assert_statement": "all(len(w) >= 4 for w in find_char_long('test words'))"
    }
  ],
  "Correctness_Score": 0.0,
  "Mutation_Score": 0.0,
  "HallucCination_Score": 1.0
}
```

---

## Import Data to MongoDB Atlas

To bulk insert your records into MongoDB Atlas, use this script.  
**Before running, modify `ATLAS_CONNECTION_STRING` with your Atlas credentials.**

```
# importToMongoDBAtlas.py

