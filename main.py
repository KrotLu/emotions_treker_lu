from flask import Flask, render_template, request
import random
from emotions import emotions_treker

app = Flask(__name__) #создаем веб-приложение
answers = ["Пон", "Окак, ну удачи тебе","Ясно.","Да мне все равно если честно", "И че"]

@app.route("/") #ловим команду
def index():
    return render_template("index.html") #загружаем главную

@app.route("/submit", methods=["POST"]) #ловим команду
def submit():
    user_message = request.form.get("message", "")
    link = '/'
    
    label, statist = emotions_treker(user_message)
    if label == "РАДОСТЬ":
        reply = "Окак, ну удачи тебе"
        link = '/fun'
    elif label == "ГРУСТЬ":
        reply = "Ну иди поплачь"
        link = '/sad'
    elif label == "СТРАХ":
        reply = "Да не парься"
        link = '/fear'
    elif label == "ЗЛОСТЬ":
        reply = "Ты это мне сказал?"
        link = '/angry'
    else:
        reply = random.choice(answers)
    
    return render_template("result.html", 
                           user_message = user_message, 
                           reply=reply,
                           link = link) #загружаем главную

@app.route("/fun") #ловим команду
def fun():
    return render_template("fun_films.html") #загружаем 

@app.route("/sad") #ловим команду
def sad():
    return render_template("sad_films.html") #загружаем 

@app.route("/fear") #ловим команду
def fear():
    return render_template("fear_films.html") #загружаем 

@app.route("/angry") #ловим команду
def angry():
    return render_template("angry_films.html") #загружаем 

if __name__ == "__main__":
    app.run(debug=True) #запускаем веб-приложение
