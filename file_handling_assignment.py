def write_to_file(filename, content):
  """Writes content to a file in write mode.

  Args:
    filename: The name of the file to write to.
    content: The content to be written to the file (string or list of strings).
  """
  try:
    with open(filename, 'w') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content)
      print(f"Successfully wrote to {filename}")
  except PermissionError:
    print(f"Error: Insufficient permissions to write to {filename}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def read_from_file(filename):
  """Reads the contents of a file and displays them on the console.

  Args:
    filename: The name of the file to read from.
  """
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      print(f"Contents of {filename}:\n{contents}")
  except FileNotFoundError:
    print(f"Error: File {filename} not found")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def append_to_file(filename, content):
  """Appends content to a file in append mode.

  Args:
    filename: The name of the file to append to.
    content: The content to be appended to the file (string or list of strings).
  """
  try:
    with open(filename, 'a') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content + "\n")
      print(f"Successfully appended to {filename}")
  except PermissionError:
    print(f"Error: Insufficient permissions to append to {filename}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

# File creation example
write_to_file("my_file.txt", [
  "This is the first line of text.\n",
  "Here's another line with a number: 42\n",
  "And a final line for good measure.\n"
])

# File reading example
read_from_file("my_file.txt")

# File appending example
append_to_file("my_file.txt", [
  "Appending some additional content.\n",
  "This line was appended using the script.\n",
  "More text to demonstrate appending.\n"
])

# Read the entire file again to show appended content
read_from_file("my_file.txt")
