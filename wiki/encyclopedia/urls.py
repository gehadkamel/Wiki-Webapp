from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
<<<<<<< HEAD
    path("test", views.test, name="test"),
]
=======
    path("wiki/<str:page>", views.entry, name="wiki"),

]
>>>>>>> 3001f176ee11bec3f7527c1400ac85204b8577a7
