from models import IQ, Family, db
from flask import Blueprint, render_template, request, redirect, url_for

iq_views = Blueprint('iq_views', __name__, template_folder='templates')


def get_user():
    return request.headers.get("Smuser", "devUser")


def make_list(input_string):
    if ',' in input_string:
        return [x.strip() for x in input_string.split(',')]
    return input_string.split()


@iq_views.route('/')
def index():
    return render_template('welcome.html')


@iq_views.route('/iq_inputs', methods=['GET', 'POST'])
def iq_inputs():
    return render_template('iq_inputs.html')


@iq_views.route('/store_iq', methods=['POST'])
def store_iq():
    print(request.form)
    first = request.form.getlist('First Name')[0]
    last = request.form.getlist('Last Name')[0]
    bday = request.form.getlist('Birth Date')[0]
    gender = request.form.getlist('Gender')[0]
    family = make_list(request.form.getlist('Family_Members')[0])
    iq = request.form.getlist('IQ')[0]

    result = IQ(first_name=first, last_name=last, birth_date=bday, gender=gender, iq_level=iq)
    db.session.add(result)

    entries = db.session.query(IQ).all()
    iq_id = max([r.id for r in entries])

    for member in family:
        attribute = Family(iq_id=iq_id, member=member)
        db.session.add(attribute)

    db.session.commit()
    return redirect(url_for('.results'))


@iq_views.route('/remove_entry/<int:iq_id>', methods=['POST', 'GET'])
def remove_entry(iq_id):
    print(iq_id)
    db.session.query(IQ).filter_by(id=iq_id).delete()
    db.session.query(Family).filter_by(iq_id=iq_id).delete()
    db.session.commit()
    return redirect(url_for('.results'))


@iq_views.route('/results')
# @login_required
def results():
    return render_template(
        'results.html',
        results=IQ.query.all())
