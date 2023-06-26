from . import views
from django.urls import path


app_name = 'hello'
urlpatterns = [
    path('', views.index, name="index"),
    path('retrieve', views.retrieve, name="retrieve"),
    path('delete', views.delete, name="delete"),
    path('index', views.index, name="index"),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup, name="signup"),
    path('librarian', views.librarian, name="librarian"),
    path('rent', views.rent, name="rent"),
    path('mail', views.mail, name="mail"),
    path('cron', views.cron_view, name="cron_view"),
    path('student', views.student, name="student"),
    path('duplicate/<str:type>/<str:value>',
         views.duplicate, name="duplicate"),
    path('update-stock', views.updateStock, name="updateStock"),
    path('retrieve2', views.retrieve2, name="retrieve2"),
    path('update', views.update, name="update"),
    path('check-login', views.checkLogin, name="checkLogin"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('fetch-rent-details', views.fetchRentDetails, name="fetchRentDetails")
]

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)"""
