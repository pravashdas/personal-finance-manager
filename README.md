# Personal Finance Manager

A simple web application for managing personal finances. Track your expenses and incomes with ease using this tool.

## Features

- **Add, Edit, and Delete Transactions:** Manage your financial records effectively.
- **Categorize Transactions:** Differentiate between expenses and incomes with categories.
- **User-friendly Interface:** Easy to navigate and manage transactions.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Database:** SQLite

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/).
- **SQLite**: Comes pre-installed with Python, but you can get more info [here](https://www.sqlite.org/index.html).

### Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/pravashdas/personal-finance-manager.git
cd personal-finance-manager

```

### Dependencies Installation
`pip install -r requirements.txt`

### Database Setup
`sqlite3 finance.db < schema.sql`

### Running the Application
`./run_app.sh`

### Alternatively, you can manually set the environment variable and start the Flask server:
`export FLASK_APP=app.py
flask run --host=0.0.0.0`

### Access the application in your web browser at
`http://localhost:5000`
