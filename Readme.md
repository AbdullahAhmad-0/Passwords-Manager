# Password Manager - Abdullah Ahmad

This is a Password Manager application developed by Abdullah Ahmad using Python, SQLite, and Tkinter. The application allows users to store and manage passwords securely in a local database. It provides a user-friendly interface with features such as adding, updating, deleting, and searching for passwords. The data can also be exported in various formats like CSV, XLSX, HTML, and TXT.

## Features

- **Add New Password**: Allows users to add new passwords by specifying details like the ID, username, password, and other custom fields.
- **Update Existing Password**: Users can update the details of an existing password.
- **Delete Password**: Option to delete a password entry from the database.
- **Search Passwords**: The app provides the ability to search for passwords based on the username.
- **Export Options**: Data can be exported in different formats such as CSV, XLSX, HTML, and TXT.
- **Import from CSV**: Users can import passwords from a CSV file into the application.
- **Clipboard Export**: Users can copy password data to the clipboard for easy pasting.
- **Settings**: Customize the labels for the last two fields in the password entry form.

## Requirements

To run this project, you'll need:

- Python 3.x
- Tkinter
- SQLite3
- PIL (Python Imaging Library)
- Pandas

You can install the required libraries using pip:

`pip install pandas pillow`

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python 3.x installed on your system.
3. Install the required libraries by running the following command:
   `pip install pandas pillow`
4. Run the script in your terminal or IDE to launch the Password Manager application.

## How to Use

1. **Launching the Application**:
   - Run script using `python main.py`
   - Once you run the script, the main window will appear. You can interact with the app by filling out the fields in the form.

2. **Adding Password**:
   - Enter the required details like Password ID, User Name, Password, and other fields, then click on **Save** to store the password.
   
3. **Updating Password**:
   - Select an existing password entry from the table, update the required fields, and click on **Update**.

4. **Deleting Password**:
   - Select a password from the table and click on **Delete** to remove it from the database.

5. **Search Password**:
   - Type the username or part of it in the search bar to find the password.

6. **Exporting Data**:
   - Use the **File** menu to export your data in various formats like CSV, XLSX, HTML, or TXT.

7. **Importing Data**:
   - You can import data from a CSV file through the **Import From CSV** option in the **File** menu.

8. **Settings**:
   - Use the **Setting** option in the **Menu** to customize the labels for the last two fields in the form.

## File Structure

- `password.icd`: SQLite database file to store the passwords.
- `set.icd`: Configuration file containing the custom labels for the last two fields in the password entry form.
- `ico.ico`: Application icon used in the window.
- `main.py`: Main Python file containing the source code for the application.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and create pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Tkinter and SQLite3 for providing the tools to build this application.
- Thanks to Pandas for its powerful data manipulation capabilities.

---

Created with ❤️ by Abdullah Ahmad
