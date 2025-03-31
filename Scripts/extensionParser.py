import typer
import os
import json

from rich import print
from pathlib import Path

app = typer.Typer()
path = Path()
file = path('ext.json')
json = file

def parseFile(json):
    load = json.loads(file)

    print(load["name"])
    print(load["type"])
    print(load["main"])

@app.command()
def load(json):
    json.load(path(file))
    