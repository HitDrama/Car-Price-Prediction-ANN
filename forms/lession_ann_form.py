from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, NumberRange
from flask_wtf.file import FileField, FileAllowed, FileRequired

class CarForm(FlaskForm):
    hang=StringField("Hãng xe",validators=[DataRequired()])
    mau=StringField("Mẫu xe",validators=[DataRequired()])
    nam=IntegerField("Năm sx",validators=[DataRequired(),NumberRange(min=2000,max=2025)])
    so_km=IntegerField("Số km",validators=[DataRequired()])
    dong_co=StringField("Động cơ",validators=[DataRequired()])
    so_cho=IntegerField("Số chỗ",validators=[DataRequired(),NumberRange(min=2,max=50)])
    mau_xe=StringField("Màu xe",validators=[DataRequired()])
    tinh_trang=SelectField("Tình trạng",choices=[("xe cũ","xe cũ"),("xe mới","xe mới")])
    loai_dong_co=SelectField("Loại động cơ",choices=[("xăng","xăng"),("dầu","dầu")])
    submit=SubmitField("Tải lên")
    