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

### If you are using TERMUX on Android then use these command for installing Python and SQLite  
```bash
pkg update && pkg upgrade
```
```bash
pkg install python sqlite
```
### Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/pravashdas/personal-finance-manager.git
cd personal-finance-manager

```

### Dependencies Installation
```bash 
pip install -r requirements.txt
```


### Database Setup
``` bash 
sqlite3 finance.db < schema.sql
```

### Give the Permission before run the Application
```bash 
chmod +x run_app.sh
```

### Running the Application
```bash 
./run_app.sh
```

### Alternatively, you can manually set the environment variable and start the Flask server:
```bash 
export FLASK_APP=app.py
flask run --host=0.0.0.0
```

### Access the application in your web browser at
`http://localhost:5000`
