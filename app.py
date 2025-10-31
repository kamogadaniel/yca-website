from flask import Flask, render_template, request, jsonify
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ==== CONFIG ====
DB_PATH = "database/contacts.db"
WHATSAPP_API_URL = "https://graph.facebook.com/v20.0"
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("YOUR_PHONE_NUMBER_ID")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# ==== DATABASE SETUP ====
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            whatsapp TEXT NOT NULL,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()


# ==== WHATSAPP FUNCTION ====
def send_whatsapp_message(name, email, whatsapp, message):
    if not (WHATSAPP_TOKEN and PHONE_NUMBER_ID):
        print("⚠️ Missing WhatsApp credentials in .env")
        return

    url = f"{WHATSAPP_API_URL}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": "YOUR_PERSONAL_WHATSAPP_NUMBER",  # replace with your verified number
        "type": "text",
        "text": {
            "body": f"📩 New YCA Contact:\n\n👤 Name: {name}\n📧 Email: {email}\n📱 WhatsApp: {whatsapp}\n📝 Message: {message}"
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print("❌ WhatsApp message failed:", response.text)
    else:
        print("✅ WhatsApp message sent successfully.")


# ==== EMAIL FUNCTION ====
def send_confirmation_email(recipient_email, recipient_name):
    if not (EMAIL_ADDRESS and EMAIL_PASSWORD):
        print("⚠️ Missing email credentials in .env")
        return

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Thank You for Reaching Out to YCA!"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email

        html = f"""
        <html>
        <body style="font-family: Arial; color: #333;">
            <h2>Dear {recipient_name},</h2>
            <p>Thank you for contacting <b>Young Christian Assembly (YCA)</b>! 🌟</p>
            <p>We’ve received your message and will get back to you soon.</p>
            <p>Stay blessed,<br><b>The YCA Team</b></p>
        </body>
        </html>
        """

        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("✅ Confirmation email sent.")
    except Exception as e:
        print("❌ Email sending failed:", e)


# ==== ROUTES ====
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/future")
def future():
    return render_template("future.html")





@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    whatsapp = data.get("whatsapp")
    message = data.get("message", "")

    # Save to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, whatsapp, message) VALUES (?, ?, ?, ?)",
              (name, email, whatsapp, message))
    conn.commit()
    conn.close()

    # Send WhatsApp message
    send_whatsapp_message(name, email, whatsapp, message)

    # Send confirmation email
    send_confirmation_email(email, name)

    return jsonify({"status": "success"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
