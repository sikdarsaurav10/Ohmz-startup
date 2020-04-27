from flask import  Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('log_in.html')

if __name__ == '__main__':
    app.run(debug=True ,port=50)