"""
Fusion Google Services MCP Server
Unified MCP server for Google Docs, Sheets, Drive, Keep, and Gmail
"""
import os
import sys
import subprocess
from mcp.server.fastmcp import FastMCP
from .config import SERVER_PORT
from .docs import read_document, append_to_document, create_document
from .sheets import read_spreadsheet, write_spreadsheet, append_spreadsheet_rows, create_spreadsheet
from .drive import list_documents, search_documents, create_folder, get_file_info
from .keep import find_notes, create_note, update_note, delete_note, get_pinned_notes
from .gmail import read_recent_emails, search_emails, send_new_email, get_full_thread

# Initialize the MCP server
mcp = FastMCP("Fusion Google Services MCP", port=SERVER_PORT)

# --- Google Docs Tools ---

@mcp.tool()
def read_google_doc(document_id: str, format: str = 'text', tab_id: str = None) -> str:
    """
    Reads the content of a specific Google Document
    
    Args:
        document_id (str): The ID of the Google Document
        format (str): Output format: 'text', 'json', or 'markdown'
        tab_id (str, optional): The ID of the specific tab to read
    """
    return read_document(document_id, format, tab_id)

@mcp.tool()
def append_to_google_doc(document_id: str, text_to_append: str, add_newline: bool = True, tab_id: str = None) -> str:
    """
    Append text to the end of a Google Document
    
    Args:
        document_id (str): The ID of the Google Document
        text_to_append (str): The text to append
        add_newline (bool): Whether to add a newline before appending
        tab_id (str, optional): The ID of the specific tab to append to
    """
    return append_to_document(document_id, text_to_append, add_newline, tab_id)

@mcp.tool()
def create_document_tool(title: str, parent_folder_id: str = None, initial_content: str = None) -> str:
    """
    Create a new Google Document
    
    Args:
        title (str): Title for the new document
        parent_folder_id (str, optional): ID of folder where document should be created
        initial_content (str, optional): Initial text content to add to the document
    """
    return create_document(title, parent_folder_id, initial_content)

# --- Google Sheets Tools ---

@mcp.tool()
def read_spreadsheet_tool(spreadsheet_id: str, range: str, value_render_option: str = 'FORMATTED_VALUE') -> str:
    """
    Read data from a specific range in a Google Spreadsheet
    
    Args:
        spreadsheet_id (str): The ID of the Google Spreadsheet
        range (str): A1 notation range to read
        value_render_option (str): How values should be rendered in the output
    """
    return read_spreadsheet(spreadsheet_id, range, value_render_option)

@mcp.tool()
def write_spreadsheet_tool(spreadsheet_id: str, range: str, values: list, value_input_option: str = 'USER_ENTERED') -> str:
    """
    Write data to a specific range in a Google Spreadsheet
    
    Args:
        spreadsheet_id (str): The ID of the Google Spreadsheet
        range (str): A1 notation range to write to
        values (list): 2D array of values to write
        value_input_option (str): How input data should be interpreted
    """
    return write_spreadsheet(spreadsheet_id, range, values, value_input_option)

@mcp.tool()
def append_spreadsheet_rows_tool(spreadsheet_id: str, range: str, values: list, value_input_option: str = 'USER_ENTERED') -> str:
    """
    Append rows of data to the end of a sheet in a Google Spreadsheet
    
    Args:
        spreadsheet_id (str): The ID of the Google Spreadsheet
        range (str): A1 notation range indicating where to append
        values (list): 2D array of values to append
        value_input_option (str): How input data should be interpreted
    """
    return append_spreadsheet_rows(spreadsheet_id, range, values, value_input_option)

@mcp.tool()
def create_spreadsheet_tool(title: str, parent_folder_id: str = None, initial_data: list = None) -> str:
    """
    Create a new Google Spreadsheet
    
    Args:
        title (str): Title for the new spreadsheet
        parent_folder_id (str, optional): ID of folder where spreadsheet should be created
        initial_data (list, optional): Initial data to populate in the first sheet
    """
    return create_spreadsheet(title, parent_folder_id, initial_data)

# --- Google Drive Tools ---

@mcp.tool()
def list_google_docs(max_results: int = 20, query: str = None, order_by: str = 'modifiedTime') -> str:
    """
    List Google Documents from Google Drive
    
    Args:
        max_results (int): Maximum number of documents to return
        query (str, optional): Search query to filter documents
        order_by (str): Sort order for results
    """
    return list_documents(max_results, query, order_by)

@mcp.tool()
def search_google_docs(search_query: str, search_in: str = 'both', max_results: int = 10, modified_after: str = None) -> str:
    """
    Search for Google Documents by name, content, or other criteria
    
    Args:
        search_query (str): Search term to find in document names or content
        search_in (str): Where to search: 'name', 'content', or 'both'
        max_results (int): Maximum number of results to return
        modified_after (str, optional): Only return documents modified after this date
    """
    return search_documents(search_query, search_in, max_results, modified_after)

@mcp.tool()
def create_drive_folder(name: str, parent_folder_id: str = None) -> str:
    """
    Create a new folder in Google Drive
    
    Args:
        name (str): Name for the new folder
        parent_folder_id (str, optional): Parent folder ID
    """
    return create_folder(name, parent_folder_id)

@mcp.tool()
def get_drive_file_info(file_id: str) -> str:
    """
    Get detailed information about a specific file in Google Drive
    
    Args:
        file_id (str): ID of the file to get information about
    """
    return get_file_info(file_id)

# --- Google Keep Tools ---

@mcp.tool()
def find_keep_notes(query: str = "") -> str:
    """
    Find notes based on a search query
    
    Args:
        query (str, optional): A string to match against the title and text
    """
    return find_notes(query)

@mcp.tool()
def create_keep_note(title: str = None, text: str = None) -> str:
    """
    Create a new note with title and text
    
    Args:
        title (str, optional): The title of the note
        text (str, optional): The content of the note
    """
    return create_note(title, text)

@mcp.tool()
def update_keep_note(note_id: str, title: str = None, text: str = None) -> str:
    """
    Update a note's properties
    
    Args:
        note_id (str): The ID of the note to update
        title (str, optional): New title for the note
        text (str, optional): New text content for the note
    """
    return update_note(note_id, title, text)

@mcp.tool()
def delete_keep_note(note_id: str) -> str:
    """
    Delete a note (mark for deletion)
    
    Args:
        note_id (str): The ID of the note to delete
    """
    return delete_note(note_id)

@mcp.tool()
def get_pinned_keep_notes(query: str = "") -> str:
    """
    Get only pinned notes
    
    Args:
        query (str, optional): A string to match against the title and text
    """
    return get_pinned_notes(query)

# --- Gmail Tools ---

@mcp.tool()
def read_recent_gmail_emails(limit: int = 10) -> str:
    """
    Fetches N most recent emails
    
    Args:
        limit (int): Number of recent emails to fetch
    """
    return read_recent_emails(limit)

@mcp.tool()
def search_gmail_emails(query: str, limit: int = 10) -> str:
    """
    Searches emails using Gmail query syntax
    
    Args:
        query (str): Gmail search query
        limit (int): Maximum number of results
    """
    return search_emails(query, limit)

@mcp.tool()
def send_gmail_email(to: str, subject: str, body: str, cc: str = "", bcc: str = "", attachments: list = []) -> str:
    """
    Sends a new email
    
    Args:
        to (str): Recipient email address
        subject (str): Email subject
        body (str): Email body
        cc (str): CC recipients
        bcc (str): BCC recipients
        attachments (list): File paths to attach
    """
    return send_new_email(to, subject, body, cc, bcc, attachments)

@mcp.tool()
def get_gmail_thread(thread_id: str) -> str:
    """
    Reads full conversation history
    
    Args:
        thread_id (str): Thread ID to read
    """
    return get_full_thread(thread_id)

# --- Server Execution ---

def main():
    """Main entry point for the Fusion Google Services MCP Server"""
    print(f"🚀 STARTING FUSION GOOGLE SERVICES MCP SERVER ON PORT {SERVER_PORT}...")
    print(f"📡 SSE Endpoint: http://127.0.0.1:{SERVER_PORT}/sse")
    print("🔔 Ensure your Client is configured to use this URL.")
    print("⌨️  Press Ctrl+C to stop.\n")
    
    try:
        # Run the server with SSE transport
        mcp.run(transport='sse')
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")

if __name__ == "__main__":
    main()