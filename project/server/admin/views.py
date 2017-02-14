from flask_admin.contrib.sqla import ModelView
# from project.server.models import *

class UserView(ModelView):
    can_edit = False
    column_exclude_list = ['password']
    column_editable_list = ['email']
    