
from flask import Flask, request

app = Flask(__name__)

# หน้าเว็บฟอร์ม
form_html = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Submit Message</title>
</head>
<body>
    <h1>Submit your message</h1>
    <form method="post">
        <textarea name="message" rows="4" cols="40" placeholder="พิมพ์ข้อความที่นี่..."></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(message + '\n')
        return f"<h1>Message received:</h1><p>{message}</p><br><a href='/'>กลับไปหน้าฟอร์ม</a>"
    return form_html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)