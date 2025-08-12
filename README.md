# PySEO

PySEO is a Python-based tool designed for web scraping and converting HTML content into Markdown format. It is particularly useful for extracting and processing web content while ignoring specific CSS classes.

## Features

- Fetch HTML content from a given URL.
- Convert HTML to Markdown format.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pyseo
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `main.py` script with the following arguments:

```bash
python main.py <url> <output_file>
```

### Example

```bash
python main.py https://example.com output.md
```

This will:
- Fetch the HTML content from `https://example.com`.
- Save the Markdown output to `output.md`.

## Development

### Running Tests

To run the test suite:

```bash
python -m unittest discover
```

### Debugging

Debugging statements can be added to `main.py` or `src/converter.py` to inspect the flow of data and function calls.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
- The Python community for their support and contributions.
