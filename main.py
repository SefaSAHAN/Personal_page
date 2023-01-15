from flask import Flask, render_template, request
from email.mime.text import MIMEText
import smtplib


app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route("/", methods=['POST','GET'])
def index():
    if request.method=="POST":
        name= request.form["name"]
        email=request.form["email"]
        text=request.form["message"]
        sender_email = "pycodersfenyx@gmail.com"
        receiver_email = "sefasahan35@gmail.com"
        password = "rvpqrzownkvhyvqz"
        subject = "This is the subject of the email"
        msg = MIMEText(f"Name: {name}\nEmail: {email}\nText: {text}")
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        try:
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("email sent successfully")
        except Exception as e:
            print("error occured:", e)
        server.quit()
        return render_template("index.html", name=name, email=email, text=text)
        
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)