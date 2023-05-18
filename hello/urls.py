from . import views
from django.urls import path

app_name = 'hello'
urlpatterns = [
    path('',views.index,name="index"),
    path('retrieve',views.retrieve, name="retrieve"),
    path('delete',views.delete, name="delete"),
    path('index',views.index,name="index"),
    path('logout',views.logout_view,name="logout"),
    path('signup',views.signup,name="signup"),
    path('librarian',views.librarian,name="librarian"),
    path('libup',views.libup,name="libup"),
    path('rent',views.rent,name="rent"),
    path('mail',views.mail,name="mail"),
    path('cron',views.cron_view,name="cron_view"),
    path('student',views.student,name="student")
]