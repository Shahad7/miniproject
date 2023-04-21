from django.contrib import admin
from .models import Book,myuser,Library,Rent

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","stock","libid")
class userAdmin(admin.ModelAdmin):
    list_display = ("id","username","name","email","role","libid")
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
class RentAdmin(admin.ModelAdmin):
    list_display = ("bid","sid")

admin.site.register(Book,BookAdmin)
admin.site.register(myuser,userAdmin)
admin.site.register(Rent,RentAdmin)
admin.site.register(Library,LibraryAdmin)

