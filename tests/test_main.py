import unittest
import argparse
import requests
from unittest.mock import patch, mock_open
from main import main

class TestMain(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args')
    @patch('main.html_to_markdown')
    @patch('requests.get')
    def test_main_success(self, mock_requests_get, mock_html_to_markdown, mock_parse_args):
        # Configure the command-line arguments
        mock_parse_args.return_value = argparse.Namespace(
            url='http://example.com',
            output_file='output.md',
            ignore_class=['ad', 'nav']
        )

        # Simulate a successful response from requests.get
        mock_response = mock_requests_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.text = "<html><body><h1>Hello World</h1></body></html>"
        
        # Simulate the result of the Markdown conversion
        mock_html_to_markdown.return_value = "# Hello World"

        # Mock the file operations
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            # Run the main function
            main()

            # Verify that requests.get was called with the correct arguments
            mock_requests_get.assert_called_once_with(
                'http://example.com', 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}, 
                timeout=10
            )

            # Verify that html_to_markdown was called with the HTML content and classes to ignore
            mock_html_to_markdown.assert_called_once_with(
                html_content="<html><body><h1>Hello World</h1></body></html>",
                ignore_classes=['ad', 'nav']
            )

            # Verify that the output file was opened and the content was written
            mock_file.assert_called_once_with('output.md', 'w', encoding='utf-8')
            mock_file().write.assert_called_once_with("# Hello World")

    @patch('requests.get')
    @patch('argparse.ArgumentParser.parse_args')
    def test_main_request_error(self, mock_parse_args, mock_requests_get):
        # Configure the arguments
        mock_parse_args.return_value = argparse.Namespace(
            url='http://invalid-url.com',
            output_file='output.md',
            ignore_class=[]
        )

        # Simulate a network error
        mock_requests_get.side_effect = requests.exceptions.RequestException

        # Capture the printed output to verify the error message
        with patch('builtins.print') as mock_print:
            main()

            # Verify that an error message was printed
            mock_print.assert_called_with(unittest.mock.ANY)
            args, _ = mock_print.call_args
            self.assertIn("Error de red o HTTP", args[0])

if __name__ == '__main__':
    unittest.main()
