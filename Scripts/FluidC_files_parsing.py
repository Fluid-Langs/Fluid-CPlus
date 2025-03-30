import typer
import os
import fs

from rich import print
from pathlib import path

app = typer.Typer()

@app.command()
def doc():
    """Display the MiniDocs for Fluid-CPlus."""
    print("""
    [bold]Fluid-CPlus MiniDocs[/bold]
    
    [underline]Overview:[/underline]
    Fluid-CPlus is a superset of C that introduces a more fluid syntax for programming.
    
    [underline]Basic Syntax:[/underline]
    - Function Declaration: 
      func functionName() {
          // function body
      }
    
    - Variable Declaration:
      let variableName = value;
    
    - Print Statement:
      print("Hello, World!");
    
    - Module Declaration:
      module ModuleName {
          // module body
      }
    
    - Using a Module:
      use ModuleName;

    [underline]Built-in Functions:[/underline]
    - print(): Outputs a string to the console.
    - let: Declares a variable.
    - return: Returns a value from a function.

    [underline]Example:[/underline]
    Here is a simple example of a Fluid-CPlus program:
    
    ```
    module MathUtils {
        func add() {
            let x = 5;
            let y = 10;
            print("Sum: " + (x + y));
            return x + y;
        }
    }
    
    use MathUtils;
    
    func main() {
        add();
    }
    ```

    [underline]Getting Started:[/underline]
    To transpile Fluid-CPlus code to C, use the following command:
    
    ```
    python fluid2c.py transpile_file input.fluid output.c
    ```

    [underline]Contributing:[/underline]
    Contributions are welcome! Please submit a pull request or open an issue on the repository.
    """)

if __name__ == "__main__":
    app()