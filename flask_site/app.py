from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret key'

posts = [
    {'id': 1, 'title': 'Post1', 'content': 'Some content1'},
    {'id': 2, 'title': 'Post2', 'content': 'Some content2'},
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post_found = list(filter(lambda p: p['id'] == post_id, posts))[0]
    return render_template('post.html', post=post_found)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            posts.append({'id': len(posts) + 1, 'title': title, 'content': content})
            flash('Save success', 'info')
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post_found = list(filter(lambda p: p['id'] == id, posts))[0]
    post_index = posts.index(post_found)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            posts[post_index] = {'id': id, 'title': title, 'content': content}
            flash('Save success', 'info')
    return render_template('edit.html', post=posts[post_index])

