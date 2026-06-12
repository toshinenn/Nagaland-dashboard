# models.py
from database import db

class GenderPopulationDecadal(db.Model):
    __tablename__ = "gender_population_decadal"

    id = db.Column(db.Integer, primary_key=True)

    year = db.Column(db.Integer)

    rural_female = db.Column(db.Integer)
    rural_male = db.Column(db.Integer)
    rural_person = db.Column(db.Integer)
    rural_sex_ratio = db.Column(db.Integer)

    urban_female = db.Column(db.Integer)
    urban_male = db.Column(db.Integer)
    urban_person = db.Column(db.Integer)
    urban_sex_ratio = db.Column(db.Integer)

    total_female = db.Column(db.Integer)
    total_male = db.Column(db.Integer)
    total_person = db.Column(db.Integer)
    total_sex_ratio = db.Column(db.Integer)

    decadal_growth_female = db.Column(db.Float)
    decadal_growth_male = db.Column(db.Float)
    decadal_growth_person = db.Column(db.Float)