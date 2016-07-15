from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class BlogForm(Form):
    title = StringField('title', [DataRequired('Title is required')])
    content = TextAreaField('content', [DataRequired('Body is required')])
    category = SelectField('category')

class SearchForm(Form):
    keyword = StringField('keyword')