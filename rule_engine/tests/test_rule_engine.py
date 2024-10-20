import unittest
from src.rule_engine import RuleEngine

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RuleEngine(':memory:')  # Use in-memory database for testing

    def test_create_rule(self):
        rule1 = self.engine.create_rule("age > 30 AND department = 'Sales'")
        self.assertEqual(rule1.type, "operator")

    def test_combine_rules(self):
        rule1 = self.engine.create_rule("age > 30 AND department = 'Sales'")
        rule2 = self.engine.create_rule("age < 25 AND department = 'Marketing'")
        combined_rule = self.engine.combine_rules([rule1, rule2])
        self.assertEqual(combined_rule.type, "operator")

    def test_evaluate_rule(self):
        rule1 = self.engine.create_rule("age > 30 AND department = 'Sales'")
        rule2 = self.engine.create_rule("age < 25 AND department = 'Marketing'")
        combined_rule = self.engine.combine_rules([rule1, rule2])
        result = self.engine.evaluate_rule(combined_rule, {"age": 35, "department": "Sales", "salary": 60000, "experience": 3})
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
