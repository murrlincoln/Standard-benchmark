import openai
import re

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_unittest_from_unorganized_tests(input_file_path, output_test_file_path):
    with open(input_file_path, 'r') as f:
        unorganized_tests = f.read()

    # Generate prompt for reformatting the tests
    prompt = f"The following Python code contains unorganized tests:\n\n{unorganized_tests}\n\nPlease reformat these tests into a unittest-compatible test.py file."

    # Generate unittest-compatible test cases using OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=500  # Adjust as necessary
    )
    organized_tests = response.choices[0].text.strip()

    # Write the organized tests to the output test file
    with open(output_test_file_path, 'w') as f:
        f.write(organized_tests)

if __name__ == "__main__":
    INPUT_UNORGANIZED_TESTS_FILE = "unorganized_tests.py"
    OUTPUT_TEST_FILE = "test.py"

    generate_unittest_from_unorganized_tests(INPUT_UNORGANIZED_TESTS_FILE, OUTPUT_TEST_FILE)
