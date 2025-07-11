from flask import Flask, render_template, request

app = Flask(__name__)

BOT_USERNAME = 'Squzeey'

@app.route('/')
def index():
    if 'tgWebAppPlatform' in request.args:
        return render_template('index.html', bot_username=BOT_USERNAME)
    else:
        return "Это должно быть открыто в Telegram Mini App."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False) # Отключите debug в production