from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(f'Logged in successfully {user.first_name}!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.myAccount'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/myAccount', methods=['GET','POST'])
@login_required
def myAccount():
    if request.method == 'POST':
        userShares = Shares.query.filter_by(id=current_user.id).first()
        sell = int(request.form.get('withdraw'))
        buy = int(request.form.get('deposit'))
        if userShares == None:
            newOwner = Shares(id = current_user.id, user_id = current_user.id, new_shares=buy, total_shares=buy)
            db.session.add(newOwner)
            db.session.commit()
        else:
            userShares.total_shares += buy
            userShares.new_shares = buy
            db.session.commit()
        print('sell is: ',sell)
    print("User id is:   ",current_user.id)
    accountValue = userShares.total_shares
    return render_template('myAccount.html', user=current_user, account= accountValue)

@auth.route('/get-started', methods=['GET', 'POST'])
def get_started():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("get_started.html", user=current_user) 
