from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, TextAreaField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Optional

class LoginForm(FlaskForm):
    """Admin login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ClientForm(FlaskForm):
    """Form for adding/editing clients"""
    name = StringField('Nama Klien', validators=[DataRequired(), Length(max=100)])
    category = SelectField('Kategori', 
                          choices=[
                              ('Food & Beverage', 'Food & Beverage'),
                              ('Lifestyle & Hospitality', 'Lifestyle & Hospitality'),
                              ('Lainnya', 'Lainnya')
                          ],
                          validators=[DataRequired()])
    emoji = StringField('Emoji', validators=[Length(max=10)], default='🏢')
    logo = FileField('Logo (Optional)', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'svg'], 'Images only!')])
    order = IntegerField('Urutan', default=0)
    is_active = BooleanField('Aktif', default=True)

class PortfolioForm(FlaskForm):
    """Form for adding/editing portfolio items"""
    title = StringField('Judul/Nama Project', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Deskripsi')
    category = SelectField('Kategori',
                          choices=[
                              ('Social Media', 'Social Media'),
                              ('Design', 'Design'),
                              ('Photography', 'Photography'),
                              ('Video', 'Video'),
                              ('Web Development', 'Web Development'),
                              ('Lainnya', 'Lainnya')
                          ])
    image = FileField('Gambar', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    order = IntegerField('Urutan', default=0)
    is_active = BooleanField('Aktif', default=True)
