from django.urls import path

from . import views

app_name = "app_quotes"

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:page>", views.main, name="main_paginate"),
    path("author/<str:author_name>", views.about_author, name="about_author"),
    path("quote/", views.quote, name="quote"),
    path("add-author/", views.author, name="author"),
]
