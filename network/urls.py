
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.createNewPost, name="post_new_post"),
    path("profile/<str:name>", views.profile_view, name="profile"),
    path("delete_post/<int:id>", views.delete_post, name="delete_post"),
    path("profile/<str:name>/follow", views.follow, name="follow"),
    path("profile/<str:name>/unfollow", views.unfollow, name="unfollow"),
    path("post/<int:id>", views.post_view, name="post"),
    path("edit_post/<int:id>", views.edit_post, name="edit_post"),
    path("search", views.search_view, name="search"),
    path("notifications", views.notifications_view, name="notifications"),
    path("like_post/<int:id>", views.like_post, name="like_post"),
    path("unlike_post/<int:id>", views.unlike_post, name="unlike_post"),
    path("comment_post/<int:id>", views.comment_post, name="comment_post"),
    path("reply_comment/<int:comment_id>", views.reply_comment, name="reply_comment"),
    path("delete_comment/<int:id>", views.delete_comment, name="delete_comment"),
]
