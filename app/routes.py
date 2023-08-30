from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import EditRecipeForm
from app.models import Recipe


@app.route('/')
@app.route('/index')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)


@app.route('/recipecard')
def recipecard():

    return render_template('recipecard.html')


@app.route('/groups')
def groups():

    return render_template('groups.html')

# @app.route('/recipecard')
# def recipecard():

#     return render_template('recipecard.html')


@app.route('/recipe/<name>')
def recipe(name):
    recipe = Recipe.query.filter_by(name=name).first_or_404()

    return render_template('recipecard.html', recipe=recipe)


@app.route('/new_recipe', methods=['GET', 'POST'])
def new_recipe():
    print("Edit recipe route accessed.")
    form = EditRecipeForm()
    if request.method == 'POST':
        print("Edit recipe route accessed2222.")
        new_recipe = Recipe(
        name=form.name.data,
        group=form.group.data,
        description=form.description.data,
        ingredients=form.ingredients.data,
        steps=form.steps.data,
        notes=form.notes.data
        )

        try:
            db.session.add(new_recipe)
            db.session.commit()
            flash('Recipe added successfully.')
            return redirect(url_for('recipecard', name=new_recipe.name))
        except Exception as e:
            print("Error:", str(e))
            db.session.rollback()  # Roll back the transaction

    return render_template('new_recipe.html', title='Edit Recipe',
                           form=form)


@app.route('/edit_recipe/<name>', methods=['GET', 'POST'])
def edit_recipe(name):
    recipe = Recipe.query.filter_by(name=name).first_or_404()
    form = EditRecipeForm(obj=recipe)  # Prepopulate the form with recipe data
    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(recipe)  # Update recipe object with form data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    return render_template('edit_recipe.html', title='Edit Recipe', form=form)
    # recipe = Recipe.query.filter_by(name=name).first_or_404()
    # form = EditRecipeForm(obj=recipe)
    # if request.method == 'POST' and form.validate_on_submit():
    #     recipe.name = form.name.data
    #     recipe.group = form.groups.data
    #     recipe.description = form.description.data
    #     recipe.ingredients = form.ingredients.data
    #     recipe.steps = form.steps.data
    #     recipe.notes = form.notes.data
    #     db.session.commit()
    #     flash('Your changes have been saved.')
    #     return redirect(url_for('edit_profile'))
    # elif request.method == 'GET':
    #     form.name.data = recipe.name
    #     form.group = recipe.groups.data
    #     form.description = recipe.description.data
    #     form.ingredients = recipe.ingredients.data
    #     form.steps = recipe.steps.data
    #     form.notes = recipe.notes.data
    #     return render_template('edit_recipe.html', title='Edit Recipe',
    #                            form=form)
