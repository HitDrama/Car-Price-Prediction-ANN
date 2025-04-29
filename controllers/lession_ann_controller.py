from flask import render_template, request, redirect, url_for,flash
from forms.lession_ann_form import CarForm
from models.price_car import Dudoangiaxe

def predict_car():
    form=CarForm()
    model=Dudoangiaxe()
    if form.validate_on_submit():
        #lấy dữ liệu từ form
        data={
            "hang":form.hang.data,
            "mau":form.mau.data,
            "nam":form.nam.data,
            "so_km":form.so_km.data,
            "dong_co":form.dong_co.data,
            "so_cho":form.so_cho.data,
            "mau_xe":form.mau_xe.data,
            "tinh_trang":form.tinh_trang.data,
            "loai_dong_co":form.loai_dong_co.data
        }
        #dự đoán giá
        ketqua=model.predict_price(data)
        #hiển thị kết quả
        flash(f"Giá xe dự đoán: {ketqua:,.0f} vnđ","success")
        return redirect(url_for("deep.predict_car"))

    return render_template("lession_ann.html",form=form)