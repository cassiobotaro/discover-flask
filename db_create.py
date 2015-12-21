from app import db
from models import BlogPost

# create the database and db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I'm Good."))
db.session.add(BlogPost("Well", "I'm well."))

# commit the changes
db.session.commit()