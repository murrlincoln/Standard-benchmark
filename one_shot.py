import json
import os
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def load_problems_from_json(json_path):
    with open(json_path, 'r') as f:
        problems = json.load(f)
    return problems

def create_and_complete_problem_file(directory, problem):
    function_name = problem['function_name']
    function_signature = problem['function_signature']
    prompt = problem['prompt']

    # Create Python file
    file_path = os.path.join(directory, f"{function_name}.py")
    with open(file_path, 'w') as f:
        f.write(f"# {function_name}\n\n")
        f.write(f"{function_signature}\n")
        f.write("# TODO: Complete this function\n")

    # Complete Python file using OpenAI API
    print(f"Completing {file_path}...")
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150  # Adjust as necessary
    )
    completed_function = response.choices[0].text.strip()

    with open(file_path, 'a') as f:
        f.write(completed_function)

# Load problems from JSON file
JSON_PATH = "problems.json"
problems = load_problems_from_json(JSON_PATH)

# The directory to save the generated Python files
DIRECTORY_PATH = "problems"

# Create and complete Python files
for problem in problems:
    create_and_complete_problem_file(DIRECTORY_PATH, problem)

print(f"Completed Python files have been saved in {DIRECTORY_PATH}.")
