from django.urls import path
from .views import index, about, portfolio, project, contact

urlpatterns = [
    path("", index, name = "home"),
    path("about/", about, name = "about"),
    path("portfolio/", portfolio, name = "portfolio"),
    path("contact/", contact, name = "contact"),
    path("portfolio/<str:project_slug>", project, name = "project"),
]
