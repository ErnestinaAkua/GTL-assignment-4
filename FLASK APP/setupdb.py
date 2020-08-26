from app import db, CountryReport

db.create_all()

Ghana = CountryReport("Ghana",20000,13000,2000,2)
Togo = CountryReport("Togo",300,130,21,0)



db.session.add_all([Ghana, Togo])

db.session.commit()


