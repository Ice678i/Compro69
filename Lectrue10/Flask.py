from Flask import flask
app = flask(__name__)
@app.route('/')
def home():
    return "คิวมวย"

if __name__ == '__main__':
    app.run(debug=True)
    