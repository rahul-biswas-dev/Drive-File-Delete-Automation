from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define the service account credentials
SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = r"path to the json file"

# Authenticate and build the Drive service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
drive_service = build("drive", "v3", credentials=credentials)


def empty_trash():
    page_token = None
    while True:
        # List trashed files with pagination
        response = (
            drive_service.files()
            .list(q="trashed=true", fields="files(id)", pageToken=page_token)
            .execute()
        )
        files = response.get("files", [])
        for file in files:
            # Delete each trashed file
            drive_service.files().delete(fileId=file["id"]).execute()
        page_token = response.get("nextPageToken")
        if not page_token:
            break


# Call the function to empty the trash


n = int(input("enter"))
for i in range(n):
    empty_trash()
