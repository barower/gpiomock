# Linux [sysfs](https://www.kernel.org/doc/Documentation/gpio/sysfs.txt) mock gpio access

This library emulates gpio access to the standard linux [sysfs interface](https://www.kernel.org/doc/Documentation/gpio/sysfs.txt)

It is a mock replacement to [gpio](https://github.com/vitiral/gpio) module. Useful when developing embedded software on local machine.

## Usage

```import gpiomock as gpio```

## Supported Features
- get pin values with `read(pin)` or `input(pin)`
- set pin values with `set(pin, value)` or `output(pin, value)`
- get the pin mode with `mode(pin)`
- set the pin mode with `setup(pin, mode)`
    - `mode` can currently equal `gpio.IN` or `gpio.OUT`
