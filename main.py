from flask import Flask, url_for, request, render_template

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


@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == "GET":
        return f"""
                <!doctype html>
                <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for("static", filename="css/style.css")}">
                        <title>Отбор астронавтов</title>
                    </head>
                    <body>
                        <h1 class="form">Анкета претендента на участие в миссии</h1>
                        <div>
                            <form class="login_form" method="post">
                                <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" 
                                name="surname">
                                <input type="text" class="form-control" id="name" placeholder="Введите имя" 
                                name="name">
                                </br>
                                
                                <input type="email" class="form-control" id="email" placeholder="Введите email" 
                                name="email" aria-describedby="emailHelp">
                                </br>
                                
                                <div class="form-group">
                                    <label for="classSelect">Какое у вас образование?</label>
                                    <select class="form-control" id="classSelect" name="class">
                                        <option>Общее</option>
                                        <option>Среднее</option>
                                        <option>Среднее профессиональное</option>
                                        <option>Высшее</option>
                                        <option>Очень высокое</option>
                                    </select>
                                </div>
                                </br>
                                
                                <label for="form-check">Какие у вас есть профессии?</label> 
                                <div class="form-group form-check" id="jobs">     
                                    <div>                   
                                        <input type="checkbox" class="form-check-input" id="job1">
                                        <label class="form-check-label" for="job1">Инженер-исследователь</label>
                                        </br>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="job2">
                                        <label class="form-check-label" for="job2">Пилот</label>
                                        </br>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="job3">
                                        <label class="form-check-label" for="job3">Строитель</label>
                                    </div>
                                </div>
                                </br>
                                
                                <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                </div>
                                </br>
                                
                                <div class="form-group">
                                    <label for="motivation">Почему именно вы должны полететь?</label>
                                    <textarea class="form-control" id="motivation" name="motivation"></textarea>
                                </div>
                                </br>
                                
                                <div class="form-group">
                                    <label for="photo">Приложите фото</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                </br>
                                
                                <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе</label>
                                </div>
                                </br>
                                
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                    </body>
                </html>
                """
    elif request.method == "POST":
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""
            <!doctype html>
            <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Варианты выбора</title>
                </head>
                <body>
                    <h1>Моё предложение - {planet_name}</h1>
                    <p class="first">Человечество вырастает из детства.</br></p>
                    <p class="second">Человечеству мала одна планета.</br></p>
                    <p class="third">Мы сделаем обитаемыми безжизненные пока планеты.</br></p>
                    <p class="fourth">И начнем с планеты {planet_name}</br></p>
                    <p class="fifth">Присоединяйся!</br></p>
                </body>
            </html>
            """


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def show_results(nickname, level, rating):
    return f"""
                <!doctype html>
                <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Результаты</title>
                    </head>
                    <body>
                        <h1>Результаты отбора претендента {nickname}</h1>
                        <p class="text-success">Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}!</p>
                        <p class="text-primary">Желаем удачи!</p>
                    </body>
                </html>
                """


@app.route("/load_photo")
def load_photo():
    return f"""
                <!doctype html>
                <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Результаты</title>
                    </head>
                    <body>
                        <h1>Загрузка фотографии для участия в миссии</h1>
                        <div class="form-group">
                                    <label for="photo">Приложите фото</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                    </body>
                </html>
                """


@app.route("/index/Заготовка")
def ind():
    return render_template("base.html", title="Заготовка")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')