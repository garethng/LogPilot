# LogPilot

![GitHub release (with filter)](https://img.shields.io/github/v/release/garethng/logpilot)
![Build Status](https://img.shields.io/github/actions/workflow/status/garethng/logpilot/python-publish.yml)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/logpilot.svg)
![GitHub issues](https://img.shields.io/github/issues/garethng/LogPilot)

## Description
LogPilot is a Python logging module that offers enhanced capabilities for logging in Python applications. It provides a simple and intuitive interface for logging, with additional features like custom fields (UUID, elapsed time), hostname inclusion, and more.

## Installation
Install LogPilot directly from PyPI:
```bash
pip install logpilot
```

## Usage
To use LogPilot in your Python projects, simply import the `Log` class and use its `get_logger` method to create a logger instance. Here's a quick start guide:

```python
from logpilot import Log

logger = Log.get_logger("your_logger_name")
logger.info("This is an info log")
logger.error("This is an error log")
```

## Features
- Easy integration with Python applications
- Automatic inclusion of hostname in logs
- Custom fields like UUID and elapsed time
- Streamlined setup of logging format and handlers

## Configuration
You can customize the logger by providing `uuid` and `elapsed` parameters when getting a logger:

```python
logger = Log.get_logger("your_logger_name", uuid="your_uuid", elapsed="time_elapsed")
```

## Removing Logger
To remove a logger instance, use the `remove_logger` method:

```python
Log.remove_logger()
```

## Requirements
- Python 3.x
- `six` library for Python 2 and 3 compatibility

## Contributing
Contributions to LogPilot are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
