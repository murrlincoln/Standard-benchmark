# Automated Python Function Generation and Testing Suite

This repository provides an end-to-end automated testing suite for Python functions. It allows you to take raw JSON files and unorganized Python tests, standardize them, generate function implementations, and finally run the tests. The suite uses OpenAI's GPT-3.5 Turbo 16k model to perform these operations.

## Features

- Standardizes raw JSON files containing problem descriptions into a unified format.
- Converts unorganized Python tests into a `unittest`-compatible `test.py` file.
- Generates Python function implementations based on standardized JSON files.
- Runs the generated `unittest`-compatible tests to validate the generated functions.

## Prerequisites

- Python 3.x
- OpenAI Python package (`openai`)
- An OpenAI API key

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/your-repo/automated-python-testing.git
    cd automated-python-testing
    ```

2. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Configuration

1. Set your OpenAI API key in the script. Replace `YOUR_OPENAI_API_KEY` with your actual API key:

    ```python
    openai.api_key = "YOUR_OPENAI_API_KEY"
    ```

2. Place your raw JSON problem descriptions in a file named `raw_problems.json`.

3. Place your unorganized test cases in a Python file named `unorganized_tests.py`.

4. Create a folder named `problems` where the Python functions will be generated.

## Usage

Run the unified script to perform all operations:

```bash
python main_script.py
```
## Output
After running the script, you'll get:

A standardized JSON file (standard_problems.json) containing the coding problems.
Python functions generated in the problems folder based on the standardized JSON.
A unittest-compatible test file (test.py) based on your unorganized tests.
Test results from running the unittests.
## How it Works
Standardization: The script first takes a raw JSON file and an unorganized Python test file. It standardizes them using OpenAI's GPT-3.5 Turbo 16k model. The standardized JSON and test files are saved as standard_problems.json and test.py, respectively.

Function Generation: The script then reads the standardized JSON file to generate Python functions. These functions are saved in individual Python files within the problems directory.

Testing: Finally, the script runs the generated unittest-compatible tests to validate the generated functions.

## Limitations and Considerations
The OpenAI GPT-3.5 Turbo 16k model has a token limit. Be cautious of this when working with large JSON files or extensive tests.

Make sure your API key is correctly set up and has sufficient API call limits for your requirements.

Given the amount of moving parts in the migrate and test one shot, it doesn't work perfectly every time. Go into the code and ensure that GPT-3.5 didn't add anything unnecessary to the functions, or responds in a way that would not align with pure code.
