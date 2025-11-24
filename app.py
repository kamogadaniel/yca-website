from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# ----------------------------------------------------
# 🔧 EMAIL CONFIGURATION (change to your real email)
# ----------------------------------------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'YOUR_EMAIL@gmail.com'  # CHANGE THIS
app.config['MAIL_PASSWORD'] = 'YOUR_APP_PASSWORD'      # CHANGE THIS
app.config['MAIL_DEFAULT_SENDER'] = 'YOUR_EMAIL@gmail.com'

mail = Mail(app)

# ----------------------------------------------------
# 🌐 ROUTES FOR WEB PAGES
# ----------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/future")
def future():
    return render_template("future.html")

@app.route("/about")
def about():
    employees = [
        {"name": "Kamoga Daniel", "job": "Lead Developer", "img": "employee1.jpg"},
        {"name": "Sarah K", "job": "Chief Councillor", "img": "employee2.jpg"},
        {"name": "Daniel K", "job": "Lead pastor", "img": "employee3.jpg"},
        {"name": "Grace L", "job": "UI/UX Designer", "img": "employee4.jpg"},
        {"name": "Andrew M", "job": "Sales Officer", "img": "employee5.jpg"},
        {"name": "Andrew M", "job": "Chief Advisor", "img": "employee5.jpg"},
        {"name": "Wayero Colline", "job": "Marketing Manager", "img": "employee5.jpg"},
        {"name": "Damba Matthuis", "job": "Music leader", "img": "employee5.jpg"},
        {"name": "Andrew M", "job": "Backend Engineer", "img": "employee5.jpg"},
        {"name": "Kabarokore Rolyne", "job": "Publicity minister", "img": "employee5.jpg"},
    ]

    members = [
        {"name": "Peter Moses", "church": "Watoto Church", "img": "member1.jpg"},
        {"name": "Ninsiima Nicole", "church": "Gaba Community Church", "img": "member2.jpg"},
        {"name": "Kamoga Daniel", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Joshua Mussiime", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Jonah K", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Mulondo Apolloo", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Nsubuga Timothy", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Nambejja Christine", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Esther Suubi", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Ntale Jonah", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Nimungu", "church": "Makerere Full Gospel", "img": "member3.jpg"},
        {"name": "Samuel K", "church": "Makerere Full Gospel", "img": "member3.jpg"},
    ]

    return render_template("about.html", employees=employees, members=members)


@app.route("/projects")
def projects():
    return render_template("projects.html")

# ====================================================
# 📩 EMAIL SENDING HELP FUNCTION
# ====================================================
def send_form_email(subject, content):
    try:
        msg = Message(subject, recipients=[app.config['MAIL_USERNAME']])
        msg.body = content
        mail.send(msg)
        return True
    except Exception as e:
        print("Email error:", e)
        return False


# ====================================================
# 🟡 1. PARTNERSHIP FORM
# ====================================================
@app.route("/send_partner", methods=["POST"])
def send_partner():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    reason = request.form["reason"]
    amount = request.form["amount"]

    content = f"""
    NEW PARTNERSHIP REQUEST

    Name: {name}
    Email: {email}
    Phone: {phone}
    Reason for Interest: {reason}
    Amount They Can Fund: {amount}
    """

    if send_form_email("New Partner Submission", content):
        return jsonify({"message": "Your partnership request has been sent successfully!"})
    return jsonify({"message": "Failed to send your request. Try again."}), 500


# ====================================================
# 🟢 2. BOARD OF GOVERNORS APPLICATION FORM
# (FIXED to match HTML)
# ====================================================
@app.route("/send_board_application", methods=["POST"])
def send_board_application():
    fullname = request.form["name"]  # FIXED
    email = request.form["email"]
    credentials = request.form["credentials"]
    letter = request.form["letter"]

    content = f"""
    NEW BOARD OF GOVERNORS APPLICATION

    Full Name: {fullname}
    Email: {email}
    Credentials: {credentials}

    Application Letter:
    {letter}
    """

    if send_form_email("Board of Governors Application", content):
        return jsonify({"message": "Your application has been sent successfully!"})
    return jsonify({"message": "Failed to send application."}), 500


# ====================================================
# 🔵 3. EMPLOYEE APPLICATION FORM
# (FIXED to match HTML)
# ====================================================
@app.route("/send_employee_application", methods=["POST"])
def send_employee_application():
    fullname = request.form["name"]  # FIXED
    email = request.form["email"]
    credentials = request.form["credentials"]
    letter = request.form["letter"]

    content = f"""
    NEW EMPLOYEE APPLICATION

    Full Name: {fullname}
    Email: {email}
    Qualifications: {credentials}

    Application Letter:
    {letter}
    """

    if send_form_email("Employee Job Application", content):
        return jsonify({"message": "Your application has been delivered successfully!"})
    return jsonify({"message": "Failed to send your application."}), 500


# ====================================================
# 🔴 4. MEMBER REGISTRATION FORM
# ====================================================
@app.route("/send_member", methods=["POST"])
def send_member():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]
    church = request.form["church"]
    reason = request.form["reason"]

    content = f"""
    NEW MEMBER REGISTRATION

    Full Name: {fullname}
    Email: {email}
    Phone: {phone}
    Church: {church}
    Reason for Joining: {reason}
    """

    if send_form_email("New Member Registration", content):
        return jsonify({"message": "Your membership request has been sent!"})
    return jsonify({"message": "Failed to send your registration."}), 500


# ----------------------------------------------------
# 🚀 RUN THE APP
# ----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
