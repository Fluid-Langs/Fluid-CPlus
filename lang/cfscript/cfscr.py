import re
import argparse
import subprocess

class CFScriptLexer:
    def __init__(self):
        self.tokens = [
            ('KEYWORD', r'\b(func|Return|typin|vary|boop)\b'),
            ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),
            ('NUMBER', r'\d+'),
            ('STRING', r'"[^"]*"'),
            ('OPERATOR', r'[+\-*/=<>!%]'),
            ('BRACKETS', r'[\(\)\[\]\{\}]'),
            ('NEWLINE', r'\n'),
            ('WHITESPACE', r'\s+'),
        ]
        self.regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.tokens)

    def tokenize(self, code):
        line_num = 1
        for match in re.finditer(self.regex, code):
            kind = match.lastgroup
            value = match.group(kind)
            if kind == 'NEWLINE':
                line_num += 1
            elif kind != 'WHITESPACE':
                yield (kind, value)


class CFScriptParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = []
        self.pos = 0

    def parse(self, code):
        self.tokens = list(self.lexer.tokenize(code))
        return self.program()

    def program(self):
        statements = []
        while self.pos < len(self.tokens):
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return statements

    def statement(self):
        token = self.current_token()
        if token[0] == 'KEYWORD' and token[1] == 'func':
            return self.function_definition()
        elif token[0] == 'KEYWORD' and token[1] == 'vary':
            return self.variable_declaration()
        elif token[0] == 'KEYWORD' and token[1] == 'Return':
            return self.return_statement()
        elif token[0] == 'KEYWORD' and token[1] == 'boop':
            return self.error_handling()
        elif token[0] == 'KEYWORD' and token[1] == 'CALL_FLUID':
            return self.call_fluid()
        else:
            return self.expression()

    def call_fluid(self):
        self.consume('KEYWORD', 'CALL_FLUID')
        file_name = self.consume('STRING')[1][1:-1]  # Strip the quotes
        return ('CALL_FLUID', file_name)

    def function_definition(self):
        self.consume('KEYWORD', 'func')
        name = self.consume('IDENTIFIER')
        self.consume('BRACKETS', '(')
        params = []
        while self.current_token()[0] != 'BRACKETS' or self.current_token()[1] != ')':
            params.append(self.consume('IDENTIFIER'))
            if self.current_token()[0] == 'OPERATOR' and self.current_token()[1] == ',':
                self.consume('OPERATOR', ',')
        self.consume('BRACKETS', ')')
        self.consume('KEYWORD', ':')
        body = self.program()
        return ('FUNC_DEF', name, params, body)

    def variable_declaration(self):
        self.consume('KEYWORD', 'vary')
        name = self.consume('IDENTIFIER')
        self.consume('OPERATOR', '>')
        value = self.expression()
        return ('VAR_DECL', name, value)

    def return_statement(self):
        self.consume('KEYWORD', 'Return')
        self.consume('OPERATOR', '(')
        value = self.expression()
        self.consume('OPERATOR', ')')
        return ('RETURN', value)

    def error_handling(self):
        self.consume('KEYWORD', 'boop')
        self.consume('OPERATOR', ':')
        try_block = self.program()
        self.consume('KEYWORD', 'except')
        error_type = self.consume('IDENTIFIER')
        self.consume('KEYWORD', 'as')
        error_name = self.consume('IDENTIFIER')
        self.consume('KEYWORD', ':')
        except_block = self.program()
        return ('BOOP', try_block, error_type, error_name, except_block)

    def expression(self):
        token = self.current_token()
        if token[0] == 'NUMBER':
            return ('NUMBER', int(self.consume('NUMBER')[1]))
        elif token[0] == 'STRING':
            return ('STRING', self.consume('STRING')[1][1:-1])  # Remove quotes
        elif token[0] == 'IDENTIFIER':
            return ('IDENTIFIER', self.consume('IDENTIFIER')[1])
        else:
            raise SyntaxError(f'Unexpected token {token}')

    def consume(self, expected_type, expected_value=None):
        token = self.current_token()
        if token[0] == expected_type and (expected_value is None or token[1] == expected_value):
            self.pos += 1
            return token
        else:
            raise SyntaxError(f'Expected {expected_type} but got {token}')

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        else:
            return None

class CFScriptInterpreter:
    def __init__(self):
        self.global_vars = {}

    def interpret(self, program):
        for stmt in program:
            self.execute(stmt)

    def execute(self, stmt):
        if stmt[0] == 'FUNC_DEF':
            name, params, body = stmt[1], stmt[2], stmt[3]
            self.global_vars[name] = ('FUNC', params, body)
        elif stmt[0] == 'VAR_DECL':
            name, value = stmt[1], self.evaluate(value)
            self.global_vars[name] = value
        elif stmt[0] == 'RETURN':
            return self.evaluate(stmt[1])
        elif stmt[0] == 'BOOP':
            try_block, error_type, error_name, except_block = stmt[1], stmt[2], stmt[3], stmt[4]
            try:
                self.interpret(try_block)
            except Exception as e:
                if e.__class__.__name__ == error_type:
                    self.interpret(except_block)
                else:
                    raise e
        elif stmt[0] == 'CALL_FLUID':
            file_name = stmt[1]
            self.call_fluid(file_name)
        else:
            raise ValueError(f'Unknown statement: {stmt}')

    def evaluate(self, expr):
        if expr[0] == 'NUMBER':
            return expr[1]
        elif expr[0] == 'STRING':
            return expr[1]
        elif expr[0] == 'IDENTIFIER':
            return self.global_vars[expr[1]]
        else:
            raise ValueError(f'Unknown expression: {expr}')
    
    def call_fluid(self, file_name):
        """
        Executes a .fluid file using a subprocess, assuming Fluid-CPlus is installed and executable.
        """
        try:
            result = subprocess.run(['fluid-cplus', file_name], capture_output=True, text=True, check=True)
            print(f"Fluid-CPlus Output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error calling {file_name}: {e.stderr}")
        except FileNotFoundError:
            print(f"Error: 'fluid-cplus' not found. Ensure Fluid-CPlus is installed.")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Run CFScript code from a file.")
    parser.add_argument('filename', help="The CFScript file to execute")
    args = parser.parse_args()

    # Read CFScript code from the specified file
    try:
        with open(args.filename, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found!")
        return
    except Exception as e:
        print(f"Error reading file '{args.filename}': {e}")
        return
    
    # Tokenize, parse, and interpret the code
    lexer = CFScriptLexer()
    parser = CFScriptParser(lexer)
    interpreter = CFScriptInterpreter()

    try:
        program = parser.parse(code)
        interpreter.interpret(program)
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == '__main__':
    main()
