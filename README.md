# Markdown Manipulator

A robust, modular Python script for batch-manipulating Markdown files in a user-specified folder. Easily extensible for any text transformation—just update the placeholder function!

## Features
- Prompts for a folder containing Markdown files (`.md`)
- Applies your custom manipulation to every file in that folder
- Strict separation of user interaction, file IO, and transformation logic
- No third-party dependencies (standard library only)

## Setup
1. Clone or download this repository.
2. Ensure you have Python 3.x installed (no pip install required).
3. (Optional) Review `requirements.txt` (should be empty or state no dependencies).

## Usage
Run the script from the command line:

```bash
python markdown-manipulator.py
```

You will be prompted to enter the path to the folder containing your Markdown files.

## Customizing Markdown Manipulation
Open `markdown-manipulator.py` and locate the `manipulate_markdown_content` function. This is a placeholder for your own logic. By default, it returns the content unchanged. Edit this function to implement any transformation you need.

**Example:**
```python
# To convert all headers to uppercase:
import re
def manipulate_markdown_content(content):
    return re.sub(r'^(#+\s*)(.*)', lambda m: m.group(1) + m.group(2).upper(), content, flags=re.MULTILINE)
```

## License
MIT
