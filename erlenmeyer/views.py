from erlenmeyer import app
from models import Post
from flask import render_template

@app.route('/')
def index():
    """Display the front page"""
    context = {
        'posts' = query_posterous.get_posts(),
        'commits' = quert_github.get_commits(),
        'title' = "Home",
    }
    return render_template('index.html', **context)
