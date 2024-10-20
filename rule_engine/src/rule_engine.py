import json
import sqlite3
from .node.py import Node

class RuleEngine:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS rules (
                                    id INTEGER PRIMARY KEY,
                                    rule_string TEXT,
                                    ast_json TEXT
                                );''')

    def create_rule(self, rule_string):
        # Parse rule_string to AST (simplified example)
        # This should be replaced with actual parsing logic
        root = Node("operator", value="AND")
        root.left = Node("operand", value="age > 30")
        root.right = Node("operand", value="department = 'Sales'")
        ast_json = json.dumps(root, default=lambda o: o.__dict__)
        with self.conn:
            self.conn.execute("INSERT INTO rules (rule_string, ast_json) VALUES (?, ?)", (rule_string, ast_json))
        return root

    def combine_rules(self, rules):
        # Combine multiple ASTs (simplified example)
        combined_root = Node("operator", value="AND")
        combined_root.left = rules[0]
        combined_root.right = rules[1]
        return combined_root

    def evaluate_rule(self, ast, data):
        # Evaluate AST against data (simplified example)
        if ast.type == "operator":
            if ast.value == "AND":
                return self.evaluate_rule(ast.left, data) and self.evaluate_rule(ast.right, data)
            elif ast.value == "OR":
                return self.evaluate_rule(ast.left, data) or self.evaluate_rule(ast.right, data)
        elif ast.type == "operand":
            # Evaluate condition (simplified example)
            return eval(ast.value, {}, data)
