import typer
import os
import fs

from rich import print
from pathlib import path

app = typer.Typer()

@app.command()
def doc():
    print(`
    [bold]Fluid-CPlus MiniDocs[/bold]
    
    `)
if __name__ == "__main__":
    app()