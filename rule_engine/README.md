# Rule Engine with AST

## Overview

This project is a simple 3-tier rule engine application that determines user eligibility based on attributes like age, department, income, spend, etc. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features

- **Rule Creation**: Create rules from strings and represent them as ASTs.
- **Rule Combination**: Combine multiple rules into a single AST.
- **Rule Evaluation**: Evaluate rules against user data.
- **Dynamic Rule Modification**: Modify existing rules dynamically.
- **Error Handling**: Handle invalid rule strings or data formats.
- **Validations**: Validate attributes to be part of a catalog.

## Project Structure
rule_engine/
│
├── database/
│   └── schema.sql
│
├── src/
│   ├── __init__.py
│   ├── node.py
│   ├── rule_engine.py
│   ├── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_rule_engine.py
│
├── requirements.txt
└── README.md

### Prerequisites

- Python 3.x
- SQLite

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/rule_engine.git
   cd rule_engine

2. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Initialize the database:
   cd database
   sqlite3 ../rules.db < schema.sql
   cd ..

### Running the Application
1. Run the main script:
   cd src
   python main.py

### Running Tests
1. Run the tests:
   python -m unittest discover -s tests
