from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask.ext.login import login_required, current_user
from .forms import BlogForm
from app.models import Blog, Category
from markdown import markdown

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

@home_blueprint.route('/')
@home_blueprint.route('/index/<int:page>')
# @login_required
def index(page=1):
    posts = Blog.query.paginate(page, app.config['POSTS_PER_PAGE'], False)
    return render_template('index.html', posts=posts, current_user=current_user)

@home_blueprint.route('/article/<article_id>')
def article(article_id):
    posts = Blog.query.filter_by(id=article_id,).all()
    return render_template('article.html', posts=posts)

@home_blueprint.route('/article/<article_id>/delete')
@login_required
def article_del(article_id):
    post = Blog.query.filter_by(id=article_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home.index'))

@home_blueprint.route('/category/<category_name>')
def category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    print category
    posts = Blog.query.filter_by(category_id=category.id).all()
    return render_template('category.html', posts=posts)

@home_blueprint.route('/publish', methods=['GET', 'POST'])
def publish():
    form = BlogForm()
    form.category.choices = [
        ('python', 'Python'),
        ('linux', 'Linux'),
        ('devops', 'DevOps')
    ]
    if form.validate_on_submit():
        current_category = Category.query.filter_by(
            name=form.category.data).first()
        format_content = markdown(request.form['content'],
            ['markdown.extensions.extra'])
        if current_category:
            post = Blog(form.title.data, format_content,
                current_user.id, current_category.id)
        else:
            current_category = Category(form.category.data)
            db.session.add(current_category)
            db.session.commit()
            post = Blog(form.title.data, format_content,
                current_user.id, current_category.id)
        db.session.add(post)
        db.session.commit()
        flash('Publish blog success!')
        return redirect(url_for('home.index'))
    return render_template('publish.html', form=form)
