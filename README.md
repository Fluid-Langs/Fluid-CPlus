# Fluid-CPlus

Fluid-CPlus is a superset of the C programming language that introduces a more fluid and expressive syntax for programming. It aims to enhance the developer experience by providing a more intuitive way to write C-like code while maintaining compatibility with existing C code.

## Features

- **Fluid Syntax**: Simplified syntax for common programming constructs.
- **Modules**: Support for modular programming with easy-to-use module declarations and imports.
- **Built-in Functions**: A set of built-in functions for common tasks, such as printing, mathematical operations, and string manipulation.
- **Configuration Management**: Use of a `fluid.yml` file for project configuration, including dependencies and project metadata.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Fluid-CPlus
   ```

2. **Install dependencies**:
   Make sure you have Python 3.6 or higher installed. You can install the required packages using pip:
   ```bash
   pip install pyyaml rich
   ```

3. **Transpiler Setup**:
   Ensure you have the transpiler set up to convert Fluid-CPlus code to C. You can use the provided `fluid2c.py` script for this purpose.

## Usage

### Writing Fluid-CPlus Code

Fluid-CPlus code is written in `.fluid` files. Here's a simple example:

```javascript
module MathUtils {
    func add() {
        let x = 5;
        let y = 10;
        print("Sum: " + (x + y));
        Return::Result(x + y);
    }
}

use MathUtils;

func main() {
    add();
}
```

### Transpiling Fluid-CPlus Code

To transpile Fluid-CPlus code to C, use the following command:

```bash
python fluid2c.py transpile_file input.fluid output.c
```

### Running a Project

You can manage your Fluid-CPlus projects using the `tasker` project manager. To create, list, and run projects, refer to the `tasker` documentation.

## Configuration

Each Fluid-CPlus project can have a `fluid.yml` configuration file that contains the following fields:

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

This project is licensed under the GPL 3.0 License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Typer](https://typer.tiangolo.com/) for creating beautiful command-line interfaces.
- [PyYAML](https://pyyaml.org/) for YAML parsing.
- [Rich](https://rich.readthedocs.io/en/stable/) for beautiful terminal output.
