import os
from flask_admin import Admin
from .models import db, User, VetModel, VetFavoriteModel, VetReviewModel, PostModel, Address
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(VetModel, db.session))
    admin.add_view(ModelView(VetFavoriteModel, db.session))
    admin.add_view(ModelView(VetReviewModel, db.session))
    admin.add_view(ModelView(PostModel, db.session))
    admin.add_view(ModelView(Address, db.session))
    # admin.add_view(ModelView(GroomerModel, db.session))
    # admin.add_view(ModelView(Groomer_Review, db.session))
    # admin.add_view(ModelView(GroomerFavoritesModel, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))