from APP_PUSHUPS import create_app, db
from APP_PUSHUPS.models import User  # If you need to import models

app = create_app()
with app.app_context():
    db.create_all()
    print("Database created successfully.")