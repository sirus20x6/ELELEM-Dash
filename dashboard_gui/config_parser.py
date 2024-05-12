import ast

def load_and_parse_ast(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    tree = ast.parse(content, filename=filepath)
    configurations = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            configurations[class_name] = {'methods': [], 'attributes': {}}
            for elem in node.body:
                if isinstance(elem, ast.FunctionDef):
                    configurations[class_name]['methods'].append(elem.name)
                elif isinstance(elem, ast.Assign):
                    for target in elem.targets:
                        if isinstance(target, ast.Name):
                            configurations[class_name]['attributes'][target.id] = 'Set manually'
                elif isinstance(elem, ast.AnnAssign):
                    if isinstance(elem.target, ast.Name):
                        configurations[class_name]['attributes'][elem.target.id] = 'Set manually'
    
    return configurations

def parse_arguments_from_class(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)

    training_args_class = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "TrainingArguments":
            training_args_class = node
            break

    if not training_args_class:
        return {}

    args = {}
    for node in training_args_class.body:
        if isinstance(node, ast.AnnAssign):
            var_name = node.target.id
            var_type = node.annotation.id if isinstance(node.annotation, ast.Name) else str(node.annotation)
            try:
                default_value = ast.literal_eval(node.value) if node.value else None
            except ValueError:
                default_value = "Complex Expression"  # Placeholder for complex types
            args[var_name] = {'type': var_type.lower(), 'default': str(default_value), 'label': var_name.replace('_', ' ').capitalize()}
    
    return args
import ast

def parse_python_file(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)
    return tree

def find_classes_with_attributes(tree):
    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_info = {
                "class_name": node.name,
                "attributes": [],
                "bases": [base.id for base in node.bases if isinstance(base, ast.Name)]
            }
            for sub_node in node.body:
                if isinstance(sub_node, ast.Assign) or isinstance(sub_node, ast.AnnAssign):
                    if isinstance(sub_node, ast.Assign):
                        # For general assignments
                        target_names = [target.id for target in sub_node.targets if isinstance(target, ast.Name)]
                    else:
                        # For annotations assignments
                        target_names = [sub_node.target.id]

                    class_info["attributes"].extend(target_names)
            classes.append(class_info)
    return classes

# Load the training_args.py AST
tree = parse_python_file(file_path)
classes_info = find_classes_with_attributes(tree)

# Display found classes and their attributes
for class_info in classes_info:
    print("Class:", class_info["class_name"])
    print("Bases:", class_info["bases"])
    print("Attributes:", class_info["attributes"], "\n")
