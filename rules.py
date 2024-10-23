import ast
from models import Node

def json_to_node(node_json):
    if node_json is None:
        return None
    return Node(
        type=node_json["type"],
        value=node_json.get("value"),
        left=json_to_node(node_json.get("left")),
        right=json_to_node(node_json.get("right"))
    )

def parse_rule(rule_string):
    """
    Parse the rule string into an AST structure.
    """
    try:
        # Parse the rule string using Python's ast module
        tree = ast.parse(rule_string, mode='eval').body

        # Recursively convert the AST into our Node structure
        return ast_to_node(tree)
    except Exception as e:
        return str(e)

def ast_to_node(tree):
    """
    Convert Python's AST structure to our custom Node structure.
    """
    if isinstance(tree, ast.BinOp):
        # If it's a binary operation (like age > 30)
        return Node(
            type="operator",
            left=ast_to_node(tree.left),
            right=ast_to_node(tree.right),
            value=type(tree.op).__name__  # Operator (e.g., 'Gt', 'Eq')
        )
    elif isinstance(tree, ast.Compare):
        # Handle comparison operations
        left = ast_to_node(tree.left)
        comparators = [ast_to_node(c) for c in tree.comparators]
        return Node(
            type="operator",
            left=left,
            right=comparators[0],  # Assuming single comparator
            value=type(tree.ops[0]).__name__  # Operator name (e.g., 'Gt')
        )
    elif isinstance(tree, ast.Name):
        # Operand is a variable (like age or department)
        return Node(type="operand", value=tree.id)
    elif isinstance(tree, ast.Constant):
        # Operand is a constant value (like 30 or 'Sales')
        return Node(type="operand", value=tree.value)
    else:
        raise ValueError(f"Unsupported AST node type: {type(tree)}")

def combine_rules_logic(rules, operator="AND"):
    """
    Combine multiple rules into a single AST using AND logic.
    """
    if not rules:
        return None

    if len(rules) == 1:
        # If there's only one rule, just return its parsed AST directly
        return parse_rule(rules[0])

    # Combine multiple rules
    root = parse_rule(rules[0])  # Parse the first rule

    for rule in rules[1:]:
        # Combine the existing AST with the new rule using 'AND'
        root = Node(
            type="operator",
            left=root,
            right=parse_rule(rule),
            value=operator  # Combine using AND operator
        )

    return root


def evaluate_rule_logic(ast, data):
    """
    Recursively evaluate the AST against the provided data.
    """

    # Debugging print statements to track what's going on
    print(f"Evaluating node: {ast}, with data: {data}")  # Debug print

    # If the node is an operand, retrieve the actual data value (e.g., 'age', 'department')
    if ast.type == "operand":
        operand_value = data.get(ast.value)
        print(f"Operand {ast.value}: {operand_value}")  # Debug print for operand
        return operand_value  # Return the value of the operand

    # If the node is an operator, evaluate left and right sub-trees based on the operator
    if ast.type == "operator":
        left_value = evaluate_rule_logic(ast.left, data)  # Evaluate the left part
        right_value = evaluate_rule_logic(ast.right, data)  # Evaluate the right part

        # Now, apply the appropriate logic based on the operator type (AND, OR, Gt, Lt, Eq)
        if ast.value == "AND":
            result = left_value and right_value  # Both must be True
            print(f"Evaluating AND: {left_value} AND {right_value} = {result}")  # Debug
            return result

        elif ast.value == "OR":
            result = left_value or right_value  # Either one must be True
            print(f"Evaluating OR: {left_value} OR {right_value} = {result}")  # Debug
            return result

        elif ast.value == "Gt":  # Greater than '>'
            result = left_value > right_value  # Compare left and right
            print(f"Evaluating Gt: {left_value} > {right_value} = {result}")  # Debug
            return result

        elif ast.value == "Lt":  # Less than '<'
            result = left_value < right_value  # Compare left and right
            print(f"Evaluating Lt: {left_value} < {right_value} = {result}")  # Debug
            return result

        elif ast.value == "Eq":  # Equals '='
            result = left_value == right_value  # Compare left and right
            print(f"Evaluating Eq: {left_value} == {right_value} = {result}")  # Debug
            return result

    # If nothing matches, return False (something went wrong)
    return False  # <-- Make sure we have a fallback return value if something goes wrong

