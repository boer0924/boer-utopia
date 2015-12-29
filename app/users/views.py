from app import db, bcrypt
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask.ext.login import login_user, login_required, logout_user, current_user
from .forms import LoginForm, RegisterForm
from app.models import User

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is not None and bcrypt.check_password_hash(
            user.password, form.password.data):
            if form.remember.data:
                login_user(user, remember=True)
            else:
                login_user(user)
            flash('Login success!')
            return redirect(url_for('home.index'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('users.login'))
    return render_template('login.html', form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.index'))

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Register success and login!')
        return redirect(url_for('home.index'))
    return render_template('register.html', form=form)

@users_blueprint.route('/user/<name>')
def profile(name):
    return render_template('profile.html', current_user=current_user)
