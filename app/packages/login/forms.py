from flask_wtf.form import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    SATELLITE_CHOICES = (
        (u"0", u"PARS1_FM"),
        (u"1", u"PARS1_DB"),
        (u"2", u"NAHID2"),
        (u"3", u"P_TEST"),
    )
    GS_CHOICES = (
        (u"0", u"Tehran"),
        (u"1", u"Tabriz"),
        (u"2", u"Gheshm"),
        (u"3", u"Mashahad"),
    )
    username = StringField(
        label='username',
        default="test",
        validators=[DataRequired(),],
    )
    satellite_name = SelectField(
        label='satellite_name',
        choices=SATELLITE_CHOICES,
        validators=[DataRequired(),],
    )
    server_name = StringField(
        label='server_name',
        default="a",
        validators=[DataRequired(),],
    )
    ground_station_name = SelectField(
        label='ground_station_name',
        choices=GS_CHOICES,
        validators=[DataRequired(), ],
    )
    password = PasswordField(
        label='password',
        default=1,
        )
    submit = SubmitField(label='login', )
