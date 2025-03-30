import re
import typer
from typing import Optional

class FluidCPlusTranspiler:
    def __init__(self):
        self.output = []

    def transpile(self, code: str) -> str:
        lines = code.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith('func'):
                self.transpile_function(line)
            elif line.startswith('let'):
                self.transpile_assignment(line)
            elif line.startswith('print'):
                self.transpile_print(line)
            elif line.startswith('module'):
                self.transpile_module(line)
            elif line.startswith('use'):
                self.transpile_use(line)
            elif line.startswith('return'):
                self.transpile_return(line)
            elif line.startswith('include'):
                self.transpile_include(line)
            else:
                self.output.append(line)  # Pass through other lines

        return "\n".join(self.output)

    def transpile_function(self, line: str):
        match = re.match(r'func (\w+)\(\) \{(.*)\}', line, re.DOTALL)
        if match:
            func_name = match.group(1)
            body = match.group(2).strip()
            self.output.append(f"void {func_name}() {{\n{body}\n}}")

    def transpile_assignment(self, line: str):
        match = re.match(r'let (\w+) = (.+);', line)
        if match:
            var_name = match.group(1)
            value = match.group(2)
            self.output.append(f"int {var_name} = {value};")

    def transpile_print(self, line: str):
        match = re.match(r'print\((.*)\);', line)
        if match:
            content = match.group(1)
            self.output.append(f'printf("{content}\\n");')

    def transpile_module(self, line: str):
        match = re.match(r'module (\w+) \{(.*)\}', line, re.DOTALL)
        if match:
            module_name = match.group(1)
            body = match.group(2).strip()
            self.output.append(f"// Module: {module_name}\n{body}")

    def transpile_use(self, line: str):
        match = re.match(r'use (\w+);', line)
        if match:
            module_name = match.group(1)
            self.output.append(f"// Using module: {module_name}")

    def transpile_return(self, line: str):
        match = re.match(r'return (.+);', line)
        if match:
            value = match.group(1)
            self.output.append(f"return {value};")

    def transpile_include(self, line: str):
        match = re.match(r'include "(.+)"', line)
        if match:
            header_file = match.group(1)
            self.output.append(f'#include "{header_file}"')

app = typer.Typer()

@app.command()
def transpile_file(input_file: str, output_file: Optional[str] = None):
    """Transpile Fluid-CPlus code from a file to C code."""
    with open(input_file, 'r') as f:
        code = f.read()

    transpiler = FluidCPlusTranspiler()
    c_code = transpiler.transpile(code)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(c_code)
        typer.echo(f"Transpiled code written to {output_file}")
    else:
        typer.echo(c_code)

@app.command()
def transpile_code(code: str):
    """Transpile Fluid-CPlus code provided as a string."""
    transpiler = FluidCPlusTranspiler()
    c_code = transpiler.transpile(code)
    typer.echo(c_code)

if __name__ == "__main__":
    app()
