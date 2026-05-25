from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

profile_bp = Blueprint('profile', __name__, template_folder='templates')

@profile_bp.route('/')
@login_required
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', current_user=current_user)
    return None

@profile_bp.route('/change-username', methods=["GET", "POST"])
def change_username():
    return render_template('change_username.html')