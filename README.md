# Fusion Google Services MCP

A unified Model Context Protocol (MCP) server that provides comprehensive access to Google Workspace services including Google Docs, Sheets, Drive, Keep, and Gmail.

## Features

- **Google Docs Integration**: Read, write, and manage Google Documents
- **Google Sheets Integration**: Read from and write to Google Spreadsheets
- **Google Drive Integration**: List, search, and organize files and folders
- **Google Keep Integration**: Create, update, and manage notes
- **Gmail Integration**: Read emails, search, and send new messages

## Prerequisites

- Python 3.8 or higher
- Google Cloud Project with appropriate APIs enabled
- OAuth2 credentials for Google Workspace access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Praveens1234/fusion-google-service-mcp.git
cd fusion-google-service-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Google credentials:
   - Create a Google Cloud Project
   - Enable the Google Docs, Sheets, Drive, Keep, and Gmail APIs
   - Download the OAuth2 credentials file
   - Place the credentials file in the project directory

## Configuration

1. Rename `config.example.py` to `config.py`
2. Update the configuration with your specific settings:
   ```python
   SERVER_PORT = 9300  # Port for the MCP server
   CREDENTIALS_FILE = "credentials.json"  # Path to your Google credentials
   ```

## Usage

1. Start the server:
```bash
python server.py
```

2. Connect your MCP client to:
```
http://localhost:9300/sse
```

## Available Tools

### Google Docs Tools
- `read_google_doc`: Read content from a Google Document
- `append_to_google_doc`: Append text to a Google Document
- `create_document_tool`: Create a new Google Document

### Google Sheets Tools
- `read_spreadsheet_tool`: Read data from a Google Spreadsheet
- `write_spreadsheet_tool`: Write data to a Google Spreadsheet
- `append_spreadsheet_rows_tool`: Append rows to a Google Spreadsheet
- `create_spreadsheet_tool`: Create a new Google Spreadsheet

### Google Drive Tools
- `list_google_docs`: List Google Documents in Drive
- `search_google_docs`: Search for specific documents
- `create_drive_folder`: Create a new folder in Drive
- `get_drive_file_info`: Get detailed information about a file

### Google Keep Tools
- `find_keep_notes`: Search for notes
- `create_keep_note`: Create a new note
- `update_keep_note`: Update an existing note
- `delete_keep_note`: Delete a note
- `get_pinned_keep_notes`: Get only pinned notes

### Gmail Tools
- `read_recent_gmail_emails`: Read recent emails
- `search_gmail_emails`: Search emails using Gmail query syntax
- `send_gmail_email`: Send a new email
- `get_gmail_thread`: Read a full email thread

## Security

- Never commit credentials files to version control
- Use appropriate OAuth2 scopes for your needs
- Regularly rotate credentials
- Implement proper access controls in production environments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.