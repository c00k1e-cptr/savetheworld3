from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/image')
def image():
    return render_template('image.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')