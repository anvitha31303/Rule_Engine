import unittest
from rules import parse_rule, combine_rules_logic,evaluate_rule_logic

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        rule = parse_rule("age > 30 AND department = 'Sales'")
        # TODO: Add assertions to verify the AST representation

    def test_combine_rule(self):
        rule1 = parse_rule("age > 30")
        rule2 = parse_rule("department = 'Sales'")
        combined_ast = combine_rules_logic([rule1, rule2], operator="AND")
        data = {"age": 35, "department": "Sales"}
        result = evaluate_rule_logic(combined_ast, data)
        assert result == True

    def test_evaluate_rule(self):
        ast = parse_rule("age > 30 AND department = 'Sales'")
        data = {"age": 35, "department": "Sales"}
        result = evaluate_rule_logic(ast, data)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
