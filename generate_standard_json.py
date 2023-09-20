import json
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_standard_json_from_raw_input(input_path, output_path):
    # Load the raw JSON data
    with open(input_path, 'r') as f:
        raw_data = json.load(f)

    # Prepare the output JSON structure
    standardized_problems = []

    for item in raw_data:
        # Convert the raw JSON item into a text string
        raw_text = json.dumps(item, indent=4)

        # Use OpenAI API to standardize the problem description, function name, and function signature
        prompt = f"Given the following raw JSON data for a coding problem:\n\n{raw_text}\n\nPlease provide a standardized description with function name, function signature, and a detailed prompt."
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=200  # Adjust as necessary
        )
        standardized_text = response.choices[0].text.strip()

        # Assume that the standardized text is in the format:
        # Function Name: xxx
        # Function Signature: xxx
        # Prompt: xxx
        lines = standardized_text.split('\n')
        function_name = lines[0].split(': ')[1].strip()
        function_signature = lines[1].split(': ')[1].strip()
        detailed_prompt = lines[2].split(': ')[1].strip()

        # Prepare the standardized problem entry
        standardized_problem = {
            "function_name": function_name,
            "function_signature": function_signature,
            "prompt": detailed_prompt
        }
        standardized_problems.append(standardized_problem)

    # Save the standardized problems to the output JSON file
    with open(output_path, 'w') as f:
        json.dump(standardized_problems, f, indent=4)

if __name__ == "__main__":
    INPUT_JSON_PATH = "raw_input.json"
    OUTPUT_JSON_PATH = "standardized_problems.json"

    generate_standard_json_from_raw_input(INPUT_JSON_PATH, OUTPUT_JSON_PATH)
