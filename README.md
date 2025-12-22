# Chainlit Tool Calling Demo

Small Chainlit app demonstrating a tool-enabled LangChain agent that returns a mock hospital patient record via `generate_patient`.

## Prerequisites
- Python 3.10+ recommended
- OpenAI API key with access to `gpt-4.1-mini`

## Installation
1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key (replace the value with your key):
   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

## Run the app
Start Chainlit and watch for changes:
```bash
chainlit run toolapp.py --watch
```

The UI will be available at http://localhost:8000. Ask about a patient; the app will call the `generate_patient` tool and return the mock record.
