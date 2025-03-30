import typer
import os
import yaml
from pathlib import Path

app = typer.Typer()

# Define the base directory for Fluid-CPlus projects
BASE_DIR = Path.home() / "Documents/Tasker/projects"

def load_project_config(project_path: Path):
    """Load the project configuration from fluid.yml."""
    config_path = project_path / "fluid.yml"
    if config_path.exists():
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        return None

@app.command()
def create_project(name: str):
    """Create a new Fluid-CPlus project."""
    project_path = BASE_DIR / name
    if project_path.exists():
        typer.echo(f"Project '{name}' already exists.")
    else:
        project_path.mkdir(parents=True, exist_ok=True)
        (project_path / f"{name}.fluid").touch()  # Create a sample Fluid-CPlus file
        
        # Create a default fluid.yml configuration file
        default_config = {
            'name': name,
            'version': '1.0.0',
            'description': f'A sample Fluid-CPlus project for {name}',
            'dependencies': []
        }
        with open(project_path / "fluid.yml", 'w') as config_file:
            yaml.dump(default_config, config_file)
        
        typer.echo(f"Project '{name}' created at {project_path} with default configuration.")

@app.command()
def list_projects():
    """List all Fluid-CPlus projects."""
    if BASE_DIR.exists():
        projects = [p.name for p in BASE_DIR.iterdir() if p.is_dir()]
        if projects:
            typer.echo("Existing Fluid-CPlus projects:")
            for project in projects:
                config = load_project_config(BASE_DIR / project)
                if config:
                    typer.echo(f"- {config['name']} (v{config['version']}): {config['description']}")
                else:
                    typer.echo(f"- {project} (No configuration found)")
        else:
            typer.echo("No Fluid-CPlus projects found.")
    else:
        typer.echo("No Fluid-CPlus projects directory found.")

@app.command()
def run_project(name: str):
    """Run a Fluid-CPlus project."""
    project_path = BASE_DIR / name
    if project_path.exists():
        config = load_project_config(project_path)
        if config:
            typer.echo(f"Running project '{config['name']}' (v{config['version']})...")
            # Here you would add logic to run the project, e.g., transpile and execute
            # Example: subprocess.run(["python", "fluid2c.py", "transpile_file", f"{project_path}/{name}.fluid", f"{project_path}/{name}.c"])
        else:
            typer.echo(f"Project '{name}' does not have a valid configuration.")
    else:
        typer.echo(f"Project '{name}' does not exist.")

if __name__ == "__main__":
    # Ensure the base directory exists
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    app()
