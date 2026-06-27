# AI Agent with Gemini

This project provides a simple yet powerful AI agent that leverages Google's Gemini model to interact with a local codebase. The agent can read files, list directory contents, execute Python scripts, and write files, allowing it to understand and modify code based on natural language prompts.

## Features

-   **Interactive:** Chat with an AI agent from your terminal.
-   **File System Access:** The agent can list, read, and write files within a specified directory.
-   **Code Execution:** It can run Python scripts and see the output.
-   **Sandboxed:** All operations are restricted to a designated working directory for safety.

## Prerequisites

-   Python 3.12 or higher
-   A Google Gemini API Key

## Setup and Installation

1.  **Clone the Repository:**
    If this project is in a git repository, clone it. Otherwise, ensure you have all the project files in a local directory.

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    The project uses `uv` for dependency management, but you can also use `pip`.

    ```bash
    # Using uv
    pip install uv
    uv pip install -r pyproject.toml

    # Or using pip directly
    pip install -e .
    ```

4.  **Set Up Your API Key:**
    The agent requires a Google Gemini API key.

    -   Create a file named `.env` in the `ai-agent` directory.
    -   Add your API key to the file like this:

    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## How to Run

You can interact with the agent by running the `main.py` script from your terminal.

```bash
python main.py "Your prompt for the AI agent"
```

**Example:**

```bash
python main.py "What is the main function in the calculator.py file?"
```

### Verbose Mode

For more detailed output, including token counts and function call details, use the `--verbose` flag:

```bash
python main.py "Can you add a new function to the calculator to handle subtraction?" --verbose
```

## Using with Your Own Codebase

This agent can be pointed at any project directory. All its operations (listing, reading, writing, and running files) are sandboxed to a specific "working directory" for safety.

### 1. Place Your Project

Place your target project folder inside the `ai-agent` directory. For example, if your project is called `my-awesome-app`, your folder structure would look like this:

```
ai-agent/
├── my-app/
│   ├── ... (your project files)
├── calculator/
├── functions/
├── main.py
└── ... (other agent files)
```

### 2. Configure the Working Directory

Next, you need to tell the agent to target your project folder instead of the default `calculator` folder.

1.  Open the file `ai-agent/call_function.py`.
2.  Find the following line inside the `call_function` function:

    ```python
    args["working_directory"] = "./calculator"
    ```

3.  Change the path `"./calculator"` to the relative path of your project directory. Following the example above, you would change it to:

    ```python
    args["working_directory"] = "./my-app"
    ```

Now, when you run the agent, it will perform all file operations within your project's directory.

## Extending the Agent with New Functions

The true power of this agent comes from its ability to call custom functions. The agent knows which functions are available based on the configuration in `ai-agent/call_function.py`.

To add a new function (e.g., `run_linter`):

1.  **Create the Function:** Create a new Python file in the `ai-agent/functions/` directory (e.g., `run_linter.py`). This file should contain two things:
    *   The function logic itself (e.g., `def run_linter(...):`).
    *   A `schema_...` variable that describes the function to the AI model, following the `google.genai.types.FunctionDeclaration` format.

2.  **Register the Function:** Open `ai-agent/call_function.py`:
    *   Import your new function and its schema at the top of the file.
    *   Add your `schema_run_linter` to the `function_declarations` list.
    *   Add your `run_linter` function to the `function_map` dictionary, mapping its name as a string to the function object.

This tells the Gemini model that your new tool exists and tells the agent how to execute it when the model decides to use it.
