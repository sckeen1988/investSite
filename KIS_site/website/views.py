from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)


@views.route('/investmentManagement')
def investmentManagement():
    print('Going to the investment management page')
    return render_template('investmentManagement.html',user=current_user)