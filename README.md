# 📝 Python Log Generator

A beginner-friendly Python project that demonstrates how to use the built-in `logging` module to record application events, warnings, errors, and file operations.

## 🚀 Features

- Records application startup and shutdown events.
- Logs user login and logout events.
- Demonstrates different logging levels: `INFO`, `WARNING`, and `ERROR`.
- Handles invalid menu inputs.
- Opens and reads text files.
- Handles missing files using exception handling.
- Stores logs in an `app.log` file with timestamps.

## 🛠️ Technologies Used

- **Python 3**
- `logging` — for recording application events.
- `os` — for retrieving the script's filename.
- File handling and exception handling.

## 📂 Project Structure

```text
log-generator/
├── main.py
├── README.md
└── .gitignore
```

The `app.log` file is generated automatically when the program runs.

## ▶️ How to Run

1. Install Python 3 if it is not already installed.
2. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

3. Navigate to the project directory:

   ```bash
   cd log-generator
   ```

4. Run the program:

   ```bash
   python main.py
   ```

5. Choose an option from the menu to generate different log events.

## 📋 Available Options

| Option | Action |
|---|---|
| 1 | Application started |
| 2 | User login |
| 3 | User logout |
| 4 | Generate a warning event |
| 5 | Generate an error event |
| 6 | Task completed |
| 7 | File opened event |
| 8 | Open a text file and handle missing files |
| 9 | Exit the application |

## 📄 Log Format

Each log entry contains a timestamp, logging level, logger name, and message.

Example:

```text
2026-10-27 10:30:00 INFO main.py: Application start
2026-10-27 10:30:05 INFO main.py: User login
2026-10-27 10:30:10 WARNING main.py: Warning event
2026-10-27 10:30:15 ERROR main.py: Error event
```

*The timestamps and messages above are examples.*

## 📚 Concepts Practiced

- Python's `logging` module
- Logging levels and log formatting
- Exception handling with `try` and `except`
- File operations using `with open()`
- Input validation
- Loops and conditional statements