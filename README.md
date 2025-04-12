# Langchain Structured Output

This repository demonstrates the use of LangChain for generating structured outputs using various schema definitions. It includes examples of using `TypedDict`, `Pydantic`, and JSON schemas to define and validate structured data.

## Features

- **TypedDict Schema**: Demonstrates how to use Python's `TypedDict` for defining structured data.
- **Pydantic Schema**: Shows how to use Pydantic models for schema validation and structured output.
- **JSON Schema**: Illustrates the use of JSON schemas for defining and validating structured data.
- **Integration with LangChain**: Uses LangChain's `with_structured_output` method to enforce schema compliance.
- **Environment Variable Management**: Uses `.env` files for managing API keys securely.

## File Architecture

The repository is organized as follows:

```
Langchain-Structured-Output/
├── .env                          # Environment variables for API keys
├── HF_login.py                   # Script for logging into Hugging Face
├── json_schema.json              # JSON schema for defining student data
├── README.md                     # Project documentation
├── requirements.txt              # List of dependencies
├── typeddict_demo.py             # Example of using TypedDict
├── with_structured_output_json.py # Example of using JSON schema with LangChain
├── with_structured_output_pydantic.py # Example of using Pydantic models with LangChain
└── with_structured_output_typeddict.py # Example of using TypedDict with LangChain
```

## Prerequisites

- Python 3.8 or higher
- Install the required dependencies listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Langchain-Structured-Output.git
   cd Langchain-Structured-Output
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with the required API keys:
   ```plaintext
   OPENAI_API_KEY = "your_openai_api_key"
   ANTHROPIC_API_KEY = "your_anthropic_api_key"
   GOOGLE_API_KEY = "your_google_api_key"
   HUGGINGFACE_API_KEY = "your_huggingface_api_key"
   ```

## Usage

### 1. TypedDict Example
Run the `typeddict_demo.py` script to see how `TypedDict` is used for defining structured data:
```bash
python typeddict_demo.py
```

### 2. Pydantic Schema Example
Run the `with_structured_output_pydantic.py` script to see how Pydantic models are used for schema validation:
```bash
python with_structured_output_pydantic.py
```

### 3. JSON Schema Example
Run the `with_structured_output_json.py` script to see how JSON schemas are used for structured output:
```bash
python with_structured_output_json.py
```

### 4. Hugging Face Login
Run the `HF_login.py` script to log in to Hugging Face using your API token:
```bash
python HF_login.py
```

## File Descriptions

- **`with_structured_output_typeddict.py`**: Demonstrates the use of `TypedDict` for structured output.
- **`with_structured_output_pydantic.py`**: Demonstrates the use of Pydantic models for structured output.
- **`with_structured_output_json.py`**: Demonstrates the use of JSON schemas for structured output.
- **`typeddict_demo.py`**: A simple example of using `TypedDict` in Python.
- **`HF_login.py`**: Script for logging into Hugging Face using an API token.
- **`json_schema.json`**: A sample JSON schema for defining student data.
- **`.env`**: Contains API keys for various integrations (not included in the repository for security reasons).
- **`requirements.txt`**: Lists all the dependencies required for the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) for providing tools to build applications with LLMs.
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation and settings management.
- [Hugging Face](https://huggingface.co/) for their open-source machine learning tools.

## Disclaimer

Ensure that sensitive information like API keys in the `.env` file is not shared publicly.
