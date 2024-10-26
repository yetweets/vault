import os
import json

def merge_json_files(folder_path: str, output_file: str):
    combined_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                try:
                    json_data = json.load(file)
                    combined_data.append(json_data)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {filename}")

    with open(output_file, 'w') as output:
        json.dump(combined_data, output, indent=4)

folder_path = 'tweets'
output_file = 'master.json'
merge_json_files(folder_path, output_file)