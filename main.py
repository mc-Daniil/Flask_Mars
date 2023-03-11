from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def start():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return "Человечество вырастает из детства.</br>" \
           "Человечеству мала одна планета.</br>" \
           "Мы сделаем обитаемыми безжизненные пока планеты.</br>" \
           "И начнем с Марса!</br>" \
           "Присоединяйся!</br>"


@app.route("/image_mars")
def image_mars():
    return f"""
            <!doctype html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <img src="{url_for("static", filename="img/mars.jpg")}" alt="Вот он - счастливчик на Марсе">
                        <figcaption>Вот он - счастливчик на Марсе</figcaption>
                    </figure>
                </body>
            </html>
            """


@app.route("/promotion_image")
def promotion_image():
    return f"""
            <!doctype html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">

                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for("static", filename="img/mars.jpg")}" alt="Вот он - счастливчик на Марсе">
                    <p class="first">Человечество вырастает из детства.</br></p>
                    <p class="second">Человечеству мала одна планета.</br></p>
                    <p class="third">Мы сделаем обитаемыми безжизненные пока планеты.</br></p>
                    <p class="fourth">И начнем с Марса!</br></p>
                    <p class="fifth">Присоединяйся!</br></p>
                </body>
            </html>
            """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')