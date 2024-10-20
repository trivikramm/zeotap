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

## Setup Instructions

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

### File Descriptions
database/schema.sql: SQL script to create the database schema.
src/init.py: Initialization file for the src package.
src/node.py: Defines the Node class for the AST.
src/rule_engine.py: Contains the RuleEngine class with methods for creating, combining, and evaluating rules.
src/main.py: Main script to run the application.
tests/test_rule_engine.py: Unit tests for the rule engine.
requirements.txt: List of dependencies required for the project.
README.md: Project documentation.

### Design Choices
AST Representation: Chosen for its flexibility in representing complex conditional rules.
SQLite: Used for storing rules and metadata due to its simplicity and ease of setup.
Modular Design: The project is divided into modules for better maintainability and scalability.

### Dependencies
sqlite3: For storing rules and metadata.

### Example Usage
### Creating a Rule
The create_rule function in src/rule_engine.py parses a rule string and generates an AST.
### Combining Rules
The combine_rules function in src/rule_engine.py merges multiple ASTs into a single AST.
### Evaluating Rules
The evaluate_rule function in src/rule_engine.py evaluates an AST against user data and returns whether the user meets the criteria.

### Running the Application
To run the application, execute the main.py script in the src directory. This will create rules, combine them, and evaluate them against sample data.
cd src
python main.py

### Running Tests
To run the unit tests, execute the following command from the project root directory:
python -m unittest discover -s tests
This will run all the test cases in the tests directory and display the results.

### Conclusion
This project provides a simple rule engine application that uses ASTs to represent and evaluate conditional rules. It includes features for rule creation, combination, evaluation, and dynamic modification. The system is designed to be extensible and can be enhanced with additional features in the future.
