from flask import Blueprint, render_template, request, redirect, url_for
import os
import json
from flask import Blueprint, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
from models import db
from models.upload import Pointers

upload = Blueprint("upload", __name__)

CREDENTIALS_FILE = "credentials.json"
SCOPES = ['https://www.googleapis.com/auth/drive.file']
FOOTAGE_FOLDER_ID = "1p5x1GcmcVgQVL1I3-ytAnY4FTmyUGhL2"


def authenticate_drive():
    """Authenticate and return Google Drive service."""
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)


def upload_to_drive(file_path, file_name):
    """Uploads file to Google Drive and returns shareable link."""
    service = authenticate_drive()
    file_metadata = {
        "name": file_name,
        "parents": [FOOTAGE_FOLDER_ID]
    }
    media = MediaFileUpload(file_path, mimetype="video/mp4")

    uploaded_file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    file_id = uploaded_file.get("id")

    # Make the file publicly accessible
    service.permissions().create(
        fileId=file_id,
        body={"role": "reader", "type": "anyone"},
    ).execute()

    return f"https://drive.google.com/file/d/{file_id}/view"


@upload.route("/upload", methods=["GET", "POST"])
def upload_page():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for('upload.upload_page'))
        
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(url_for('upload.upload_page'))
        
        filename = secure_filename(file.filename)
        file_path = os.path.join("uploads", filename)
        file.save(file_path)
        
        # Upload to Google Drive
        drive_link = upload_to_drive(file_path, filename)
        
        # Save to Database
        new_video = Pointers(
            title=request.form.get("video_title",""),
            link=drive_link,
            description=request.form.get("video_caption", ""))
        db.session.add(new_video)
        db.session.commit()
        flash("File uploaded successfully!")
        redirect(url_for('upload.upload_page')) 
        
    return render_template("upload.html")

