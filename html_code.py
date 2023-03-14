from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/sample_page')
def return_sample_page():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='MARS.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <br><label>Вот она какая, красная планета.</label>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8084, host='127.0.0.1')