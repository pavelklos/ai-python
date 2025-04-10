# TODO: run web server by Flask
# > flask --app server run			        # run app
# > flask --app server run --debug		    # run app in debug mode
# > python -m flask --app server run	    # run app
#   Running on http://127.0.0.1:5000

from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)                         # __main__

# TODO: root '/' route
@app.route("/")                         # decorator (higher order function)
def hello_world():
    # return "<p>Hello, World!</p>"
    # TODO: Jinja (template engine)
    print(url_for('static', filename='flash.ico'))      # /static/flash.ico
    return render_template('index.html')

# TODO: '/test' route
@app.route("/test/<username>/<int:post_id>")            # TODO: Jinja (variable rules)
def test(username=None, post_id=None):
    # return "<i>TEST</i>"
    print(username)
    print(post_id)
    return render_template('test.html', name=username, id=post_id)

# TODO: '/blog' route
@app.route('/blog')
def blog():
    return '<u>This is my blog section!</u>'

@app.route('/blog/2020/dog')
def blog_dog():
    return 'This blog is about my dog, Rocky!'

# TODO: '/about' route
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':              # check if this file is run directly
    app.run()
