from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class IQ(db.Model):
    """
    Store Data pertinent to identifying factors related to low/high IQ
    """
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    iq_level = db.Column(db.Integer, nullable=False)


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iq_id = db.Column(db.Integer, db.ForeignKey(IQ.id), nullable=False)
    member = db.Column(db.String, nullable=False)