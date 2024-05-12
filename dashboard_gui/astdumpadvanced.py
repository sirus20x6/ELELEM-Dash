import ast

class ASTInterpreter:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self.tree = ast.parse(file.read(), filename=filepath)

    def parse(self):
        return self.visit(self.tree)

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        if isinstance(node, list):
            return [self.visit(n) for n in node]
        elif hasattr(node, "_fields"):
            return {field: self.visit(getattr(node, field)) for field in node._fields}
        else:
            return None

    def visit_Module(self, node):
        return self.visit(node.body)

    def visit_ClassDef(self, node):
        return {
            "name": node.name,
            "bases": [self.visit(b) for b in node.bases],
            "body": self.visit(node.body)
        }

    def visit_FunctionDef(self, node):
        return {
            "name": node.name,
            "args": self.visit(node.args),
            "body": self.visit(node.body),
            "returns": self.visit(node.returns)
        }

    def visit_AnnAssign(self, node):
        return {
            "target": node.target.id,
            "annotation": self.visit(node.annotation),
            "value": self.visit(node.value)
        }

    def visit_Assign(self, node):
        return {
            "targets": [self.visit(t) for t in node.targets],
            "value": self.visit(node.value)
        }

    def visit_Constant(self, node):
        return node.value

    def visit_Name(self, node):
        return node.id

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'field':
            # Handle 'field' calls specifically for default values in dataclasses
            kwargs = {kw.arg: self.visit(kw.value) for kw in node.keywords}
            return kwargs.get('default', 'Field without default')
        return "Complex Function Call"

# Example usage
interpreter = ASTInterpreter('/thearray/git/transformers/src/transformers/training_args.py')
parsed_data = interpreter.parse()
print(parsed_data)
