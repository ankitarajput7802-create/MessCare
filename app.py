import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("messcare.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint_type TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


init_db()   # ✅ function ke bahar


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/complaint")
def complaint():
    return render_template("complaint.html")

@app.route("/view-complaints")
def view_complaints():
    conn = sqlite3.connect("messcare.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")
    complaints = cursor.fetchall()

    conn.close()

    return render_template("complaints.html", complaints=complaints)
@app.route("/submit-complaint", methods=["POST"])
def submit_complaint():
    complaint_type = request.form["complaint_type"]
    description = request.form["description"]
    conn = sqlite3.connect("messcare.db")
    cursor = conn.cursor()
    cursor.execute(
    "INSERT INTO complaints (complaint_type, description) VALUES (?, ?)",
    (complaint_type, description)
    
    )
    conn.commit()
    conn.close()
    return f"Complaint: {complaint_type}<br>Description: {description}"