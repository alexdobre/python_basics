from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret key'

people = [
    {'id': 1, 'name': 'Alex', 'description': 'the coder', 'favorite_number': 42},
    {'id': 2, 'name': 'John', 'description': 'the unknown', 'favorite_number': 1},
]


@app.route('/')
def person_list():
    return render_template('person_list.html', people=people)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        favorite_number = int(request.form['favorite_number'])

        if not name:
            flash('Name is required!')
        else:
            people.append({
                'id': len(people) + 1,
                'name': name,
                'description': description,
                'favorite_number': favorite_number
            })
            flash('Save success', 'info')
    return render_template('person_create.html')


@app.route('/<int:person_id>/edit', methods=('GET', 'POST'))
def edit(person_id):
    person_index = -1
    for i, p in enumerate(people):
        if person_id == p['id']:
            person_index = i
            break

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        favorite_number = int(request.form['favorite_number'])

        if not name:
            flash('Name is required!')
        else:
            people[person_index] = {
                'id': len(people) + 1,
                'name': name,
                'description': description,
                'favorite_number': favorite_number
            }
            flash('Save success', 'info')
    return render_template('person_edit.html', person=people[person_index])

