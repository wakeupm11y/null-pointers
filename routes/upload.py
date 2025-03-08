from flask import Blueprint, render_template, request, redirect, url_for

upload = Blueprint("upload", __name__)

@upload.route("/upload", methods=["GET", "POST"])
def upload_page():
    # if request.method == "POST":
    #     # Handle file upload logic
    #     return redirect(url_for("upload.upload_page"))  # Redirect after successful upload
    return render_template("upload.html")
