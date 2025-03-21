# How to load Json file from local

![Screenshot 2568-03-21 at 22 18 30](https://github.com/user-attachments/assets/dd80c97a-f543-4ad0-960a-d79c3699bbf2)


```
import json
```

`pandas (pd)` → Used for handling structured data (like tables, CSVs, and JSONs).

- `json` → Standard Python module for working with JSON data.

```
def import_json(json_file_name):
```
Defines a function named `import_json` that takes one parameter:

- `json_file_name:` A string representing the file path of the JSON file to be loaded.

```
try:
```

- Starts a `try` block to catch errors that may occur while processing the JSON file.

```
with open(json_file_name, 'r') as file:
    data = file.read()
```

- `open(json_file_name, 'r')` → Opens the JSON file in read mode ('r').
- `file.read()` → Reads the entire content of the file into the variable data as a string.

```
json_data = json.loads(data)

```
- `json.loads(data)` → Parses the JSON-formatted string (data) and converts it into a Python dictionary (json_data).

```
except ValueError as e:
    print(f"Error reading JSON file: {e}")
    return {}
```

- If an invalid JSON file is provided, the function:
1. Catches the ValueError.
2. Prints an error message (Error reading JSON file: <error message>).
3. Returns an empty dictionary ({}) instead of crashing.
