from flask import Flask, render_template

app = Flask(__name__)

# Пример данных
news_data = [
    {"id": 1, "title": "Что-то не работает? Напиши в тех.поддержку!", "description": "Наша тех.поддержка доступна в телеграмм: https://t.me/CarlSupport_bot", "image": "/static/news1.jpg"},
    {"id": 2, "title": "Подписывайся на нас в Telegram!", "description": "Да, да у нас есть Telegram канал! https://t.me/carlbrawlru", "image": "/static/CarlBrawl.jpg"}
]

video_data = [
    {"id": 1, "title": "Трейлер обновления", "description": "Смотрите наш новый трейлер!", "image": "/static/video1.jpg"},
    {"id": 2, "title": "Геймплей сезона", "description": "Узнайте больше о новом сезоне.", "image": "/static/video2.jpg"}
]

main_news = {
    "id": 0,
    "title": "Добро пожаловать в Sazium Brawl!",
    "description": "Играй и побеждай в новой игре от CarlTeam!",
    "image": "/static/coming.png"
}

@app.route("/")
def home():
    return render_template(
        "index.html",
        main_news=main_news,
        news=news_data,
        videos=video_data
    )

@app.route("/news/<int:news_id>")
def news_details(news_id):
    # Поиск новости по ID
    selected_news = next((news for news in news_data if news["id"] == news_id), None)
    if not selected_news:
        return "Новость не найдена", 404
    return render_template("news_details.html", news=selected_news)

if __name__ == "__main__":
    app.run(debug=True)
