import pandas as pd

from flask import Flask
from database import db
from models import GenderPopulationDecadal

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///population.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

EXCEL_FILE = "1_PopulationBirths_DeathsRelated_2024.xlsx"

def clean_float(value):
    if pd.isna(value):
        return None

    value = str(value).strip()
    value = value.replace(",", "")
    value = value.replace("(-)", "-")

    try:
        return float(value)
    except ValueError:
        return None

def clean_int(value):
    num = clean_float(value)
    if num is None:
        return None
    return int(num)


def seed_p1():
    df = pd.read_excel(EXCEL_FILE, sheet_name="P-1", header=None)

    # Actual data rows: 1971 to 2011
    data_rows = df.iloc[4:9]

    GenderPopulationDecadal.query.delete()

    for _, row in data_rows.iterrows():
        record = GenderPopulationDecadal(
            year=clean_int(row[1]),

            rural_female=clean_int(row[2]),
            rural_male=clean_int(row[3]),
            rural_person=clean_int(row[4]),
            rural_sex_ratio=clean_int(row[5]),

            urban_female=clean_int(row[6]),
            urban_male=clean_int(row[7]),
            urban_person=clean_int(row[8]),
            urban_sex_ratio=clean_int(row[9]),

            total_female=clean_int(row[10]),
            total_male=clean_int(row[11]),
            total_person=clean_int(row[12]),
            total_sex_ratio=clean_int(row[13]),

            decadal_growth_female=clean_float(row[14]),
            decadal_growth_male=clean_float(row[15]),
            decadal_growth_person=clean_float(row[16])
        )

        db.session.add(record)

    db.session.commit()
    print("P-1 Gender Population Decadal seeded successfully.")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_p1()