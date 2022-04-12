# Add any form classes for Flask-WTF here
from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from wtforms import StringField,FileField,SubmitField
from wtforms.validators import DataRequired,FileRequired

images = UploadSet('images', IMAGES)

class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired()])
    photo = FileField('image',validators=[FileRequired(),FileAllowed(images, 'Images only!')])
    submit = SubmitField('Submit')