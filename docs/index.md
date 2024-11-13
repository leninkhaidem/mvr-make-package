# MVR Make Package

This tool automates the generation of a boilerplate folder structure and essential files based on user input, specifically designed for the MVR framework. It simplifies the process of setting up a new package with the required structure and configuration files, allowing developers to focus on implementing their core functionality.

## Overview

The `mvr-make-package` tool is designed to:

- Generate a standardized folder structure for MVR packages.
- Populate each folder with boilerplate files.
- Automatically configure files with initial content based on user input.

This tool ensures that all necessary components for an MVR package are in place, enabling seamless integration into the MVR framework.

## Installation

<!-- termynal -->
```console
$ pip install mvr-make-package

---> 100%
```

## Usage

To create a new MVR package, simply run `mvr-make-package`

You will be prompted to provide the following information:

- Package Name: The name of your MVR package (e.g., mvr-hello-world).
- Minimum NCS Version: The minimum supported version of the NCS framework (e.g., 5.0).
- Package Description: A brief description of the package (e.g., This package provides hello world functionality for MVR).

The tool will use these inputs to generate the folder structure and populate the files with initial content based on your responses.

### Example

```console
$  mvr-make-package


╭────────────────────────────────── Welcome ───────────────────────────────────╮
│                           mvr-make-package - 0.0.1                           │
│                                                                              │
│ This tool generates a folder structure with boilerplate files based on user  │
│                input. This will be used by the MVR framework                 │
╰─────────────────────────── Generating packages... ───────────────────────────╯


  [1/3] name of the mvr package (mvr package name): mvr-hello-world
  [2/3] mininum ncs version (5.0): 
  [3/3] mvr package description (package description): mvr hello world example
🎉 Package generated successfully! 🎉
```

After running this command, a new folder called `mvr-hello-world` will be created with the standard folder structure.

### Generated Folder Structure

```console
mvr-hello-world
├── package-meta-data.xml
├── python
│   └── mvr_hello_world
│       ├── __init__.py
│       ├── correlators
│       │   ├── __init__.py
│       │   └── c_1.py
│       ├── extractions
│       │   ├── __init__.py
│       │   ├── dx_1.py
│       │   └── dx_2.py
│       ├── mvr_hello_world.py
│       ├── template_engines.py
│       └── yang_inputs.py
├── src
│   ├── Makefile
│   └── yang
│       └── mvr-hello-world.yang
└── templates
    └── mvr-hello-world-template.xml
```

## Testing

This project includes automated tests to verify the integrity of the generated package. The tests check that:

- All expected files are generated.
- The contents of each file match the predefined templates (using file hash comparison).

### Running Tests

To run the tests, use `pytest`. Install using `pip install pytest` if not already installed.

<!-- termynal -->
```console
$ cd tests
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.9.10, pytest-8.3.3, pluggy-1.5.0
rootdir: mvr-make-package
configfile: pyproject.toml
plugins: cov-6.0.0, anyio-4.6.2.post1
collected 13 items                                                             

test_mvr_make_package.py .............                                   [100%]

============================== 13 passed in 0.20s ==============================
```

## Contributing

Contributions are welcome! If you’d like to improve the tool or add new features, please:

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request.

Please make sure to add tests for any new features and update the README if necessary.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/leninkhaidem/mvr-make-package/blob/main/LICENSE) file for details.
