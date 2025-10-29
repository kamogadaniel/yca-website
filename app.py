from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from twilio.rest import Client
import os

app = Flask(__name__)

# ====== CONFIGURATION ======
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email setup (you can use Gmail or another SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USER')  # your email address
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASS')  # your app password

db = SQLAlchemy(app)
mail = Mail(app)

# Twilio setup (WhatsApp)
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH = os.getenv('TWILIO_AUTH')
TWILIO_FROM = 'whatsapp:+14155238886'  # Twilio sandbox
MY_WHATSAPP = 'whatsapp:+256XXXXXXXXX'  # your WhatsApp number with country code
client = Client(TWILIO_SID, TWILIO_AUTH)


# ====== DATABASE MODEL ======
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    whatsapp = db.Column(db.String(50))
    message = db.Column(db.Text)

with app.app_context():
    db.create_all()


# ====== ROUTES ======
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/future')
def future():
    return render_template('future.html')

@app.route('/about')
def about():
    return render_template('about.html')


# ====== FORM SUBMISSION ======
@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        name = request.form['name']
        email = request.form['email']
        whatsapp = request.form['whatsapp']
        message = request.form.get('message', '')

        # Save to database
        new_contact = Contact(name=name, email=email, whatsapp=whatsapp, message=message)
        db.session.add(new_contact)
        db.session.commit()

        # Send confirmation email to user
        msg = Message(
            subject="Thank You for Contacting YCA!",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email],
            body=f"Hello {name},\n\nWe’re glad you reached out to Young Christian Assembly! "
                 f"Our team will contact you soon.\n\nGod bless you!\nYCA Team"
        )
        mail.send(msg)

        # Send WhatsApp message to you (admin)
        client.messages.create(
            from_=TWILIO_FROM,
            to=MY_WHATSAPP,
            body=f"📩 New YCA Contact:\nName: {name}\nEmail: {email}\nWhatsApp: {whatsapp}\nMessage: {message}"
        )

        return jsonify({"success": True}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
