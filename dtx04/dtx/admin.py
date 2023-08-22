from django.contrib import admin
from .models import User, Plan, Result, Counseling, User_consultant, User_Medical

admin.site.register(User)
admin.site.register(User_consultant)
admin.site.register(User_Medical)
admin.site.register(Plan)
admin.site.register(Result)
admin.site.register(Counseling)

# Register your models here.
