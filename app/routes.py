from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import EditProfileForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')


@app.route('/recipecard')
def recipecard():

    return render_template('recipecard.html')

@app.route('/groups')
def groups():

    return render_template('groups.html')

# @app.route('/recipecard')
# def recipecard():

#     return render_template('recipecard.html')



@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('user.html', user=user)


@app.route('/edit_recipe', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    # if form.validate_on_submit():
    #     current_user.username = form.username.data
    #     current_user.about_me = form.about_me.data
    #     db.session.commit()
    #     flash('Your changes have been saved.')
    #     return redirect(url_for('edit_profile'))
    # elif request.method == 'GET':
    #     form.username.data = current_user.username
    #     form.about_me.data = current_user.about_me
    return render_template('edit_recipe.html', title='Edit Profile',
                           form=form)
