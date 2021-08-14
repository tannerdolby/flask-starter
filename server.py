from flask import Flask, request, render_template
from datetime import datetime
import re

# Create the Flask App
app = Flask(__name__)

# Helpers (Context processors and filters for template usage)

# Provide a template variable with a datetime.utcnow() object
@app.context_processor
def inject_date():
    return {
        "date": datetime.utcnow()
    }

@app.context_processor
def inject_name():
    return {
        "fname": "Tanner",
        "lname": "Dolby"
    }

@app.add_template_filter
def slugify(s):
    return re.sub(r"[\s]+", "-", s.lower())

# Handle Routing

# Root URL route ie '/'
@app.route('/', methods=["GET", "POST"])
def index():
    """Displays the index page at root url '/'"""
    return render_template("index.html",
        projects=[
            {
                "name": "Prime Number Generator",
                "date": "2021-08-13",
            },
            {
                "name": "PyPi Plugin",
                "date": "2021-08-25",
            },
            {
                "name": "Matrix library",
                "date": "2021-08-07"
            }
        ]
    )

# Blog posts

posts = [
    {
        "name": "Getting Started with Flask",
        "date": "2021-08-13",
        "image": "https://images.pexels.com/photos/5726693/pexels-photo-5726693.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "html": "<p>Flask is a lightweight web framework. It honestly provides so much that you might sometimes forget it is leaner than other frameworks</p>"
    },
    {
        "name": "Some other cool post about Python and Flask",
        "date": "2021-08-25",
        "image": "https://images.pexels.com/photos/1181671/pexels-photo-1181671.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "html": "<p>When a framework makes developing applications easier for the developer. That is usually desired. Flask does exactly this. It provides the tools and features for a fast development cycle.</p>"
    },
    {
        "name": "Using Web Frameworks like Flask",
        "date": "2021-08-07",
        "image": "https://images.pexels.com/photos/1181373/pexels-photo-1181373.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "html": "<p>Web frameworks provide the tools we need to more quickly build web applications with languages like Python (Flask, Django) or JavaScript (Node.js, Next.js etc).</p>"
    }
]

@app.route('/blog')
def blog(title=None):
    "Displays the page for '/blog' URL"
    return render_template('blog.html', posts=posts)



@app.route('/blog/<title>')
def post(title=''):
    selected = {}
    pos = 0
    slugs = [re.sub(r"[\s]+", "-", post["name"]) for post in posts]

    for post in posts:
        if (title == re.sub(r"[\s]+", "-", post["name"].lower())):
            selected = post
            pos = posts.index(selected)

    print(selected)

    return render_template('post.html', post=selected, posts=posts, pos=pos)

@app.route('/contact')
def about():
    "Displays the page for '/contact' URL"
    return render_template('contact.html', socials=[
        {
            "name": "GitHub",
            "url": "https://github.com/tannerdolby"
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/tannerdolby"
        },
        {
            "name": "CodePen",
            "url": "https://codepen.io/tannerdolby"
        }
    ])

if __name__ == '__main__':
    app.debug = True
    app.run()