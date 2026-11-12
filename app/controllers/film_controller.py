from flask import Blueprint, render_template, request, redirect, url_for
from app.models.film import FilmModel, Actor

film_bp = Blueprint('film', __name__)

film_model = FilmModel()


@film_bp.route('/')
def index():
    films = film_model.get_all_films()
    return render_template('index.html', films=films)


@film_bp.route('/add', methods=['GET', 'POST'])
def add_film():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        director = request.form['director']
        year = int(request.form['year'])
        duration = int(request.form['duration'])
        studio = request.form['studio']

        actors = []

        names = request.form.getlist('actor_name')
        roles = request.form.getlist('actor_role')

        for name, role in zip(names, roles):
            if name.strip() and role.strip():
                actors.append(Actor(name, role))

        film_model.add_film(
            title, genre, director,
            year, duration, studio, actors
        )

        return redirect(url_for('film.index'))

    return render_template('add_film.html')


@film_bp.route('/delete/<int:film_id>')
def delete_film(film_id):
    film_model.delete_film(film_id)
    return redirect(url_for('film.index'))