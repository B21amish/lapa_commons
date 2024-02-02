# lapa_commons

## About

Lapa commons used for reading the configuration file.

## Installation

> pip install lapa_commons

## Env

- python>=3.12.0

## Changelog

### v0.0.1

1. configparser added in the dependency.
2. Function read_configuration_from_file_path() added which reads the configuration from a filepath.
3. Support for any number of sections in the configuration file.
4. Environment section variables will be first checked in the OS, if not found in the OS then it will be read from the configuration file.
5. MODULE_NAME added in the **init**.py
