from .rule_engine import RuleEngine

# Example usage
engine = RuleEngine('rules.db')
rule1 = engine.create_rule("age > 30 AND department = 'Sales'")
rule2 = engine.create_rule("age < 25 AND department = 'Marketing'")
combined_rule = engine.combine_rules([rule1, rule2])
result = engine.evaluate_rule(combined_rule, {"age": 35, "department": "Sales", "salary": 60000, "experience": 3})
print(result)
