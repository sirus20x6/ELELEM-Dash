import ast

file_path = '/thearray/git/transformers/src/transformers/training_args.py'

import ast

def evaluate_expression(node):
    """
    Evaluates an expression in a limited and controlled fashion.
    """
    if isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.NameConstant):
        return node.value
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        operand = evaluate_expression(node.operand)
        return +operand if isinstance(node.op, ast.UAdd) else -operand
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)
        return left + right
    elif isinstance(node, ast.Dict):
        return {evaluate_expression(k): evaluate_expression(v) for k, v in zip(node.keys, node.values)}
    elif isinstance(node, ast.List):
        return [evaluate_expression(elem) for elem in node.elts]
    elif isinstance(node, ast.Tuple):
        return tuple(evaluate_expression(elem) for elem in node.elts)
    return "Complex Expression"

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


def parse_configurations(ast_data):
    categories = {
        'Basic Training': ['learning_rate', 'batch_size', 'num_train_epochs'],
        'Evaluation': ['eval_strategy', 'eval_steps'],
        'Advanced Optimization': ['adam_epsilon', 'lr_scheduler_type'],
        'System Settings': ['log_level', 'use_cpu'],
        'Data Handling': ['dataloader_num_workers', 'remove_unused_columns']
    }
    categorized_settings = {category: {} for category in categories}
    
    for setting in ast_data:
        for category, settings in categories.items():
            if setting['name'] in settings:
                categorized_settings[category][setting['name']] = setting['default']
    
    return categorized_settings





