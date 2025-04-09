from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Obsidian's Flask</h1><p>This is a comment inside the Flask</p><p>This is another comment inside the Flask</p>"

if __name__ == "__main__":
    app.run()