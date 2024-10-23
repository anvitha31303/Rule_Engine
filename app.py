from flask import Flask, request, jsonify, render_template
import psycopg2
from rules import parse_rule, combine_rules_logic, evaluate_rule_logic, json_to_node


app = Flask(__name__)


# Database connection
def get_db_connection():
    conn = psycopg2.connect("dbname=rule_engine_db user=postgres password=Postgre")
    return conn


# Render the main HTML page
@app.route('/')
def index():
    return render_template('index.html')


# Create a rule and return its AST
@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.json
    rule_string = data.get("rule")

    if not rule_string:
        return jsonify({"error": "No rule provided"}), 400

    # Parse the rule and convert it into a Node
    ast = parse_rule(rule_string)

    if isinstance(ast, str):  # If there was an error, it would return a string
        return jsonify({"error": "Invalid rule", "details": ast}), 400

    # Convert the Node object to a dictionary
    return jsonify({"ast": ast.to_dict()})

# Combine rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    data = request.get_json()
    rules = data.get("rules", [])

    # Combine rules using the 'combine_rules_logic' function
    combined_ast = combine_rules_logic(rules)

    if isinstance(combined_ast, str):  # Error case
        return jsonify({"combined_ast": combined_ast}), 400
    else:
        # Return the combined AST as a properly formatted JSON response
        return jsonify({"combined_ast": combined_ast.to_dict()})


# Evaluate rule against JSON data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    # Fetch the incoming JSON payload
    payload = request.json
    print(f"Incoming payload: {payload}")

    # Extract 'ast' and 'data' from the payload
    ast = payload.get('ast')
    data = payload.get('data')

    # Ensure the 'ast' and 'data' are present in the payload
    if not ast or not data:
        return jsonify({"error": "Invalid payload. 'ast' and 'data' are required."}), 400

    # Evaluate the AST
    try:
        if ast['value'] == "AND":
            # Evaluate both sides of the AND condition
            left = evaluate_condition(ast['left'], data)
            right = evaluate_condition(ast['right'], data)
            result = left and right
        else:
            result = False  # Handle other cases (e.g., OR, NOT, etc.)
    except KeyError as e:
        # Catch missing keys and return an error message
        return jsonify({"error": f"KeyError: Missing key {str(e)} in the AST or data."}), 400

    # Return the evaluation result as JSON
    return jsonify({"result": result})
def evaluate_operand(operand, data):
    if operand['type'] == 'operand':
        return data.get(operand['value'], None)
    return None

def evaluate_condition(condition, data):
    if condition['type'] == 'operator':
        operator = condition['value']

        # Get left operand's value (e.g., "age" or "department")
        left_value = condition['left']['value']

        # Fetch the actual data value for the left operand (e.g., 35 for age, "Sales" for department)
        left_operand = data.get(left_value, None)

        # Ensure left operand exists in the data
        if left_operand is None:
            print(f"Error: Left operand '{left_value}' not found in the data.")
            return False

        # Get right operand's value (this could be a constant like 30 or "Sales")
        right_operand = condition['right']['value']

        print(f"Evaluating condition: {condition}")
        print(f"Left operand ({left_value}): {left_operand}")
        print(f"Right operand: {right_operand}")
# Evaluate the condition based on the operator
        if operator == 'Gt':  # Greater than
            return left_operand > right_operand
        elif operator == 'Ge':  # Greater than or equal to
            return left_operand >= right_operand
        elif operator == 'Lt':  # Less than
            return left_operand < right_operand
        elif operator == 'Le':  # Less than or equal to
            return left_operand <= right_operand
        elif operator == 'Eq':  # Equals
            return left_operand == right_operand
        elif operator == 'Ne':  # Not equals
            return left_operand != right_operand
        else:
            print(f"Error: Unknown operator '{operator}'.")
            return False

    return False  # Default to False if condition type is not an operator



if __name__ == '__main__':
    app.run(debug=True)