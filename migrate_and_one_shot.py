import json
import unittest
import os
import openai
import re

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Standardize the raw JSON
def generate_standard_json_from_raw_input(input_path, output_path):
    with open(input_path, 'r') as f:
        raw_data = json.load(f)
    standardized_problems = []
    for item in raw_data:
        raw_text = json.dumps(item, indent=4)
        prompt = f"Given the raw JSON data:\n\n{raw_text}\n\nStandardize it into a coding problem with function name, function signature, and a detailed prompt."
        response = openai.Completion.create(engine="gpt-3.5-turbo-16k", prompt=prompt, max_tokens=15000)
        standardized_text = response.choices[0].text.strip()
        lines = standardized_text.split('\n')
        function_name = lines[0].split(': ')[1].strip()
        function_signature = lines[1].split(': ')[1].strip()
        detailed_prompt = lines[2].split(': ')[1].strip()
        standardized_problem = {"function_name": function_name, "function_signature": function_signature, "prompt": detailed_prompt}
        standardized_problems.append(standardized_problem)
    with open(output_path, 'w') as f:
        json.dump(standardized_problems, f, indent=4)

# Standardize the unorganized test Python file
def generate_unittest_from_unorganized_tests(input_file_path, output_test_file_path):
    with open(input_file_path, 'r') as f:
        unorganized_tests = f.read()
    prompt = f"The following Python code contains unorganized tests:\n\n{unorganized_tests}\n\nPlease reformat these tests into a unittest-compatible test.py file."
    response = openai.Completion.create(engine="gpt-3.5-turbo-16k", prompt=prompt, max_tokens=15000)
    organized_tests = response.choices[0].text.strip()
    with open(output_test_file_path, 'w') as f:
        f.write(organized_tests)

# Generate Python functions based on standardized JSON
def create_and_complete_problem_file(directory, problem):
    function_name = problem['function_name']
    function_signature = problem['function_signature']
    prompt = problem['prompt']
    file_path = os.path.join(directory, f"{function_name}.py")
    with open(file_path, 'w') as f:
        f.write(f"# {function_name}\n\n")
        f.write(f"{function_signature}\n")
        f.write("# TODO: Complete this function\n")
    full_prompt = f"{prompt}\n\n{function_signature}  # TODO: Complete this function"
    response = openai.Completion.create(engine="gpt-3.5-turbo-16k", prompt=full_prompt, max_tokens=10000)
    completed_function = response.choices[0].text.strip()
    with open(file_path, 'a') as f:
        f.write(completed_function)

# Run unittests
def run_tests(test_path):
    test_file_path = os.path.join(test_path, 'test.py')
    if os.path.exists(test_file_path):
        loader = unittest.TestLoader()
        suite = loader.discover(test_path, pattern='test.py')
        runner = unittest.TextTestRunner()
        runner.run(suite)
    else:
        print(f"No test.py found in {test_path}")

if __name__ == "__main__":
    # Step 1: Standardize the raw JSON and unorganized tests
    INPUT_RAW_JSON_PATH = "raw_problems.json"
    OUTPUT_STANDARD_JSON_PATH = "standard_problems.json"
    INPUT_UNORGANIZED_TESTS_FILE = "unorganized_tests.py"
    OUTPUT_TEST_FILE = "test.py"
    generate_standard_json_from_raw_input(INPUT_RAW_JSON_PATH, OUTPUT_STANDARD_JSON_PATH)
    generate_unittest_from_unorganized_tests(INPUT_UNORGANIZED_TESTS_FILE, OUTPUT_TEST_FILE)

    # Step 2: Generate Python functions
    problems = json.load(open(OUTPUT_STANDARD_JSON_PATH, 'r'))
    DIRECTORY_PATH = "problems"
    for problem in problems:
        create_and_complete_problem_file(DIRECTORY_PATH, problem)

    # Step 3: Run the tests
    TEST_DIRECTORY_PATH = "tests"
    run_tests(TEST_DIRECTORY_PATH)
