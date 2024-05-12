import ast

def dump_ast_of_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    tree = ast.parse(content, filename=file_path)
    return ast.dump(tree, indent=4)  # Use indent for better readability

def save_ast_dump_to_file(file_path, output_path):
    ast_representation = dump_ast_of_file(file_path)
    with open(output_path, 'w') as out_file:
        out_file.write(ast_representation)

# Call the function to save the dump
input_path = '/thearray/git/transformers/src/transformers/training_args.py'  # The actual path to your training_args.py
output_path = './output_ast_dump.txt'  # Path where you want to save the AST dump
save_ast_dump_to_file(input_path, output_path)
