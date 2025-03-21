import json

def import_json(json_file_name):
    try:
        with open(json_file_name, 'r') as file:
            data = file.read()
            json_data = json.loads(data)
            return json_data
    except ValueError as e:
        print(f"Error reading JSON file: {e}")
        return {}
