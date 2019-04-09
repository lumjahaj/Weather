
class WeatherForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    country = TextAreaField('Country', validators=[DataRequired()])
    submit = SubmitField('Get Weather')
