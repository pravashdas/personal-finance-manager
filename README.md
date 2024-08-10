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

## Installation For Termux(Android) and Debian based OS

Follow these steps to set up the project locally.

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/).
- **SQLite**: Comes pre-installed with Python, but you can get more info [here](https://www.sqlite.org/index.html).


# Instructions for Android Systems

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

### Give the Permission before run the Application
```bash 
chmod +x run_app.sh
```

### Running the Application
```bash 
./run_app.sh
```

### Alternatively, you can manually set the environment variable and start the Flask server:
 
`export FLASK_APP=app.py`
`flask run --host=0.0.0.0`


### Access the application in your web browser at
`http://localhost:5000`

# Instructions for Debian-based Systems
### Update the Package List and Upgrade Installed Packages
```bash
sudo apt update && sudo apt upgrade
```

### Install Python and SQLite
```bash
sudo apt install python3 sqlite3
```

### Clone the Repository
```bash
git clone https://github.com/pravashdas/personal-finance-manager.git
```
```bash
cd personal-finance-manager
```

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Give Permission to Run the Application
```bash
chmod +x run_app.sh
```

### Running the Application
```bash
./run_app.sh
```
### Alternatively, you can manually set the environment variable and start the Flask server:
`export FLASK_APP=app.py`
`flask run --host=0.0.0.0`

### Access the application in your web browser at
`http://localhost:5000`



# Instructions for Windows Systems

### Install Python and SQLite

1. Download and install Python from the official website: https://www.python.org/downloads/
2. Download and install SQLite from the official website: https://www.sqlite.org/download.html

### Clone the Repository
``` bash
git clone https://github.com/pravashdas/personal-finance-manager.git
```

``` bash
cd personal-finance-manager
```

### Install Dependencies
``` bash
pip install -r requirements.txt
```


### Running the Application

If using Command Prompt or PowerShell:
``` bash
python run_app.py
```
### Alternatively, you can manually set the environment variable and start the Flask server:
``` bash
set FLASK_APP=app.py
flask run --host=0.0.0.0
``` 

### Access the application in your web browser at
``` bash
http://localhost:5000
``` 
