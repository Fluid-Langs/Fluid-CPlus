# Tasker - Project Manager for Fluid-CPlus

Tasker is a command-line project manager for Fluid-CPlus, a superset of C that introduces a more fluid syntax for programming. This tool allows you to create, manage, and run Fluid-CPlus projects easily.

## Features

- Create new Fluid-CPlus projects with a default configuration.
- List existing Fluid-CPlus projects.
- Run Fluid-CPlus projects (with placeholder functionality for transpiling and executing).

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd tasker
   ```

2. **Install dependencies**:
   Make sure you have Python 3.6 or higher installed. You can install the required packages using pip:
   ```bash
   pip install typer pyyaml rich
   ```

## Usage

### Create a New Project

To create a new Fluid-CPlus project, use the following command:

```bash
python -m tasker.app create-project <project_name>
```

This will create a new directory for the project and a default `fluid.yml` configuration file.

### List Existing Projects

To list all existing Fluid-CPlus projects, run:

```bash
python -m tasker.app list-projects
```

This will display the names, versions, and descriptions of all projects in the base directory.

### Run a Project

To run a specific Fluid-CPlus project, use:

```bash
python -m tasker.app run-project <project_name>
```

This command will check for the project's configuration and provide feedback.

## Configuration

Each Fluid-CPlus project has a `fluid.yml` configuration file that contains the following fields:

- **name**: The name of the project.
- **version**: The version of the project.
- **description**: A brief description of the project.
- **dependencies**: A list of dependencies required by the project.

### Example `fluid.yml`

```yaml
name: MyFluidProject
version: 1.0.0
description: A sample Fluid-CPlus project
dependencies:
  - fluid-lib1
  - fluid-lib2
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Typer](https://typer.tiangolo.com/) for creating beautiful command-line interfaces.
- [PyYAML](https://pyyaml.org/) for YAML parsing.
- [Rich](https://rich.readthedocs.io/en/stable/) for beautiful terminal output.
