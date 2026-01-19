from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = "ayomidepeculiar82@gmail.com"
EMAIL_PASSWORD = "Oluwaseun 1....."

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json

    msg = EmailMessage()
    msg["Subject"] = f"New Portfolio Message — {data['name']}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    msg.set_content(f"""
Name: {data['name']}
Email: {data['email']}
Project Type: {data['project']}
Budget: {data['budget']}

Message:
{data['message']}
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
