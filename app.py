from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Sorry Message</title>
    </head>
    <body>
        <h1>I&#39;m sorry 😔🙏</h1>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run()


