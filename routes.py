from flask import Blueprint
from controllers.lession_ann_controller import predict_car


deep_router=Blueprint("deep",__name__)

#định nghĩa router
deep_router.route("/",methods=["GET","POST"])(predict_car)