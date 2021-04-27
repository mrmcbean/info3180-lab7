from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired, InputRequired


class UploadForm(FlaskForm):
    description = TextAreaField("Enter Description",validators=[InputRequired()])

    photo=FileField("Upload Image", validators=[
        FileRequired(),
        FileAllowed(['jpg','png','jpeg', 'Images only!'])
    ])
    
    

    

