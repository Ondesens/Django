from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.home, name="home"),  # 👈 теперь главная
    path("blog/", views.index, name="index"),  # список новостей
    path("detail/<int:pk>/", views.detail, name="blog_detail"),
    path("create/", views.create_blog, name="blog_create"),
    path("update/<int:pk>/", views.update_blog, name="update_blog"),
    path("delete/<int:pk>/", views.delete_blog, name="delete_blog"),
    path("contacts/", views.contacts, name="contacts"),
]
