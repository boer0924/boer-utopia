from app import app, db
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask.ext.login import login_required, current_user
from .forms import BlogForm, SearchForm
from app.models import Blog, Category, User
from markdown import markdown
from sqlalchemy import desc
from datetime import datetime

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

@home_blueprint.route('/', methods=['GET', 'POST'])
@home_blueprint.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    form = SearchForm()
    if form.validate_on_submit():
        results = Blog.query.filter(Blog.content.like('%' + form.keyword.data + '%'))
        if results.all():
            posts = results.paginate(page, app.config['POSTS_PER_PAGE'], False)
            hot_posts = Blog.query.order_by(desc(Blog.pub_date)).limit(app.config['HOT_POSTS_COUNT']).all()
            return render_template('index.html', posts=posts, hot_posts=hot_posts, form=form)
        else:
            flash('Not found with [' + form.keyword.data + '] blog.')
            return redirect(url_for('home.index'))
    posts = Blog.query.order_by(desc(Blog.pub_date)).paginate(page, app.config['POSTS_PER_PAGE'], False)
    hot_posts = Blog.query.order_by(desc(Blog.pub_date)).limit(app.config['HOT_POSTS_COUNT']).all()
    return render_template('index.html', posts=posts, hot_posts=hot_posts, form=form)

@home_blueprint.route('/article/<article_id>')
def article(article_id):
    post = Blog.query.filter_by(id=article_id,).first()
    format_content = markdown(post.content, ['markdown.extensions.extra'])
    return render_template('article.html', post=post, content=format_content)

@home_blueprint.route('/article/<article_id>/edit', methods=['GET', 'POST'])
def article_edit(article_id):
    form = BlogForm()
    post = Blog.query.filter_by(id=article_id,).first()
    choices = Category.get_all()
    form.category.choices = choices
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.author_id = current_user.id
        post.category_id = form.category.data
        post.pub_date = datetime.utcnow()
        db.session.add(post)
        db.session.commit()
        flash('Update blog sucessfully!')
        return redirect(url_for('home.article', article_id=post.id))   
    form.title.data = post.title
    form.content.data = post.content
    form.category.data = post.category_id
    return render_template('publish.html', form=form)

@home_blueprint.route('/article/<article_id>/delete')
@login_required
def article_del(article_id):
    post = Blog.query.filter_by(id=article_id).first()
    if current_user.name == post.author.name or current_user.name == 'boer':
        db.session.delete(post)
        db.session.commit()
        flash('Delete blog success!')
        return redirect(url_for('home.index'))
    else:
        flash('You are not Superuser!')
        return redirect(url_for('home.index'))

@home_blueprint.route('/category/<category_name>')
def category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    posts = Blog.query.filter_by(category_id=category.id).all()
    return render_template('category.html', posts=posts)

@home_blueprint.route('/publish', methods=['GET', 'POST'])
def publish():
    form = BlogForm()
    choices = Category.get_all()
    form.category.choices = choices
    if form.validate_on_submit():
        post = Blog(form.title.data, form.content.data, current_user.id, form.category.data)
        db.session.add(post)
        db.session.commit()
        flash('Publish blog success!')
        return redirect(url_for('home.index'))
    return render_template('publish.html', form=form)
