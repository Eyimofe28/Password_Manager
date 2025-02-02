# Password Manager


## Project Overview

This project is a Python-based password manager with a graphical user interface (GUI) built using Tkinter. The application allows users to generate secure passwords, save them along with website and email information in a JSON file, and retrieve them when needed. The generated passwords are automatically copied to the clipboard for easy use.

## Features

1. **Password Generation**: Generate secure passwords with a mix of letters, numbers, and symbols.
2. **Password Storage**: Save website, email, and password information in a JSON file.
3. **Password Retrieval**: Search and retrieve stored passwords.
4. **Clipboard Integration**: Automatically copy the generated password to the clipboard for easy pasting.

## Dependencies

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Pyperclip (for clipboard functionality)
- JSON (for storing and retrieving password data)

## File Descriptions

### `main.py`

This file contains the main logic and GUI setup for the password manager application. It includes functions for generating passwords, saving passwords, searching for passwords, and setting up the user interface.

### `logo.png`

An image file used as the logo for the application, displayed in the GUI.

### `data.json`

A JSON file where the saved password information is stored. Each entry includes the website, email, and password.

## Getting Started

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**: Ensure all dependencies are installed. You can install `pyperclip` using pip:
   ```bash
   pip install pyperclip
   ```

3. **Run the Project**: Execute the `main.py` file to start the application.
   ```bash
   python main.py
   ```

## Usage

1. **Generate Password**: Click the "Generate Password" button to create a new password. The generated password will be automatically copied to the clipboard.
2. **Save Information**: Enter the website, email/username, and password. Click the "Save Info!" button to save the information to `data.json`.
3. **Search for Password**: Enter the website and click the "Search" button to retrieve the stored email and password for that website.
4. **Clipboard Integration**: The generated password will be automatically copied to the clipboard for easy use.

## Code Explanation

### Password Generation

The `generate_password` function creates a secure password using a mix of letters, numbers, and symbols. The password is copied to the clipboard and displayed in the password entry field.

### Saving Password

The `save` function validates the input fields and saves the website, email, and password information to `data.json`. If any field is empty, it shows an error message.


### Finding Password

The `find_password` function searches for the stored email and password for a given website in `data.json`.



### UI Setup

The UI setup uses Tkinter to create the main window, labels, entry fields, and buttons.


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure your code follows the project’s coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This comprehensive readme should help you understand the structure and functionality of my password manager application. If you have any questions or need further assistance, please feel free to reach out :)
