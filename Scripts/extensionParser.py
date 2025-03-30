import typer
import os
import fs

from rich import print
from pathlib import path

app = typer.Typer()

@app.command()
def cc(path):
    open(path)

if __name__ == "__main__":
    app()