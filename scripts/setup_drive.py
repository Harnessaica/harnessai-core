"""
setup_drive.py — Creates the HarnessAI Google Drive folder structure.
Run once. Safe to re-run (checks for existing folders before creating).
"""
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load credentials from Backyard Leisure project (reuses existing OAuth setup)
REPO_ROOT = Path(r"C:\Users\ty\Tyrell's Projects Claude")
load_dotenv(REPO_ROOT / ".env")
sys.path.insert(0, str(REPO_ROOT))

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

PARENT_FOLDER_ID = "1DOwSDk90yhDWlhujUYktEouDZ8HmNpB0"

FOLDERS = [
    "00-Admin",
    "01-Brand",
    "02-Sales",
    "03-Clients",
    "04-Operations",
]

def get_drive_service():
    token_path = REPO_ROOT / "token.json"
    creds = Credentials.from_authorized_user_file(str(token_path))
    return build("drive", "v3", credentials=creds)

def folder_exists(service, name, parent_id):
    query = f"name='{name}' and '{parent_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
    results = service.files().list(q=query, fields="files(id,name)").execute()
    return results.get("files", [])

def create_folder(service, name, parent_id):
    existing = folder_exists(service, name, parent_id)
    if existing:
        print(f"  [=] Already exists: {name} ({existing[0]['id']})")
        return existing[0]["id"]
    metadata = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id],
    }
    folder = service.files().create(body=metadata, fields="id").execute()
    print(f"  [+] Created: {name} ({folder['id']})")
    return folder["id"]

if __name__ == "__main__":
    print("Setting up HarnessAI Google Drive folders...")
    service = get_drive_service()
    for folder_name in FOLDERS:
        create_folder(service, folder_name, PARENT_FOLDER_ID)
    print("\nDone. Open Google Drive to verify.")
