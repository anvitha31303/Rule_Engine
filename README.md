Application 1: Rule Engine with AST
Zeotap | Software Engineer Intern | Assignment | Application 1

My Intro
Hello! I'm Anvitha Guduru, a Python Full-Stack Developer skilled in React, Flask, .NET, AngularJS, and SQL. I'm currently working on projects like a Leave Management System and am always eager to learn and innovate!

---Introduction
This project develops a simple 3-tier Rule Engine application that includes a UI, API, and Backend Data. The system determines user eligibility based on various attributes such as age, department, income, and spending. It utilizes an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, combination, and modification of these rules.

===Technical Parts
Installation: Backend (Flask)
---Database (PostgreSQL):
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

---File Structure
Below is the file structure of the project:
rule_engine/
│
├── app.py                    # Main entry point for the Flask application
├──database.py                # Database connection and session management 
├──config.py                  #all configurations needed
├── models.py                 # Database schema (Rule and User models)
├── ast.py                    # Implementation of the Abstract Syntax Tree
├── rule_service.py           # Functions for rule creation, combination, and evaluation
├──requirements.txt
├── tests/ test_rules.py
├── static/                   # Static files for UI
│   └── index.html            # Frontend for interacting with the rule engine
└── test_evaluate_rule         

----API Routes
The system uses the following Flask routes for handling user interactions:

/create_rule/ - POST: Accepts a rule string and returns the corresponding AST as a Node object.
/combine_rules/ - POST: Combines a list of rule strings into a single AST and returns the root node.
/evaluate_rule/ - POST: Evaluates a given AST against user attributes to determine eligibility.

----Solution Overview
This project addresses the challenge of evaluating user eligibility based on dynamic rules. Key features include:

#Dynamic Rule Creation: Users can create rules using a string representation.
#Rule Combination: Combines multiple rules efficiently to minimize redundant checks.
#AST Representation: Represents rules in an Abstract Syntax Tree format for easy evaluation and manipulation.

--Sample Rules
Here are examples of rules that the system can handle:
Rule 1: ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
Rule 2:((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)

----API Design Endpoints
--POST /create_rule/
Description: Accepts a rule string and returns a Node object representing the AST.
Example Payload: { "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))" }

--POST /combine_rules/
Description: Combines multiple rule strings into a single AST.
Example Payload: { "rules": ["rule1", "rule2"] }

--POST /evaluate_rule/
Description: Evaluates the AST against provided user attributes.
Example Payload: { "data": { "age": 35, "department": "Sales", "salary": 60000, "experience": 3 } }

---AST Representation
Node Structure:
type: String indicating the node type ("operator" for AND/OR, "operand" for conditions).
left: Reference to another Node (left child).
right: Reference to another Node (right child for operators).
value: Optional value for operand nodes (e.g., number for comparisons).
##Sample Data Structure

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # Left child node
        self.right = right  # Right child node (for operators)
        self.value = value  # Value for operand nodes

---Non-Technical Parts
##My Approach
Understanding Requirements: The first step was to grasp the core problem of building a rule engine capable of evaluating user eligibility based on dynamic rules.
AST Implementation: I developed an efficient data structure to represent the AST and allow for dynamic rule modification.
API Design: Designed API endpoints for rule creation, combination, and evaluation.
Testing: Implemented extensive test cases to ensure the correctness of rule evaluation and handling of invalid inputs.

##Feedback
This assignment was an excellent opportunity to deepen my understanding of rule engines and ASTs, along with working on API design and implementation. The modular structure of the Flask backend made the system efficient and easy to maintain.

##Outro
This project showcases my skills in building a dynamic rule engine using Python and Flask. I look forward to any feedback and further discussions. Thank you for reviewing my work!        

