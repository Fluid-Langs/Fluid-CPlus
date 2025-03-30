## Hii! it's me, **SufremOak**, i'm gonna teach you how to install and use **Fluid-CPlus**!

### Installation (POSIX Compliant or UNIX-based/like OSes)

```bash
# Clone the repository
$ git clone https://github.com/fluid-langs/fluid-cplus.git
$ cd fluid-cplus
# install the dependencies:
# Debian and derivates
$ sudo apt install python3.12 just gcc build-essential
# ArchLinux
$ sudo pacman -S python3 just gcc
# macOS
$ brew install gcc python3 just
# Termux-Android
$ pkg install clang just python3
# install python dependencies
$ pip install -r requirements.txt
# build
$ just
# now install
$ just install
# Note: on termux or other OSes that have a read-only root, need to install on a different prefix like ~/.local/bin
# Install the general-poru-compiler (gpc)
$ cd gpc
$ npm install
$ npm install -g .
# or
$ npm link
```

> [!NOTE]
> Soon i will make some installation scripts to make the installation more automated, don't worry, it will be cross-plataform (excluding Windows (bleh))

### How-to time!!
Here you will learn how to make a **Fluid-CPlus** program

- first create a project with `tasker` or just use `gpc` to compile and run Fluid files

```sh
$ tasker new helloapp
$ cd helloapp
$ touch main.fluid
```

```javascript
// main.fluid
#include <FluidLand.h>

module main() { // main module
    let message = "Hello, World!" // create message variable
    Return::Var(new message()) // export it as a variable in the module
}

use main // import your module

func main() { // main function
    print(${message}) // print the message variable in the main module
    exir // end the program
}
```
Compiling and running
```sh
# method 1: tasker
$ tasker build --debug
$ tasker run
Hello, World!
# method 2: gpc compiler
$ gpc main.fluid --on-the-fly-compile
GPC Compiler JIT v0.1.1
?found: { module: "main" }
?log: Hello, World!
exit.
```
