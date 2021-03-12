from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        geslo = request.form.get('geslo')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, geslo):
                flash('Vpisan!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Napacno geslo', category='error')
        else:
            flash('Uporabnik ne obstaja', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required # more bit vpisaan uporabnik
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        ime = request.form.get('ime')
        geslo1 = request.form.get('geslo1')
        geslo2 = request.form.get('geslo2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Uporabnik ze obstaja', category='error')
        elif geslo1 != geslo2:
            flash("Gesli se ne ujemata", category='error') # da javi da je napaka
        elif len(geslo1) < 7:
            flash("Geslo prekratko", category='error') # da javi da je napaka
        else:
            # dodamo uporabnika v bazo
            novi_user = User(email=email, ime = ime, password=generate_password_hash(geslo1, method='sha256'))
            db.session.add(novi_user)
            db.session.commit()
            login_user(novi_user, remember=True)
            flash("Racun ustvarjen", category='success') 
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)