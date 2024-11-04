from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json

from .models import *


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")




def createNewPost(self, request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.POST)

    caption = data.get("caption", "")
    hashtags = data.get("hastags", {})
    media = data.get("media", None)

    post = Posts(
        caption = caption,
        hashtags = hashtags,
        media = media,
        creator = request.user,
    )

    post.save()

    return HttpResponseRedirect(reverse("index"))

def profile_view(request, name):
    profile = User.objects.get(username = name)

    posts_profile = Posts.objects.filter(creator = profile)

    return render(request, "network/profile.html", {
        "profile": profile,
        "posts": posts_profile,
    })

def follow(request, name):
    return 201

def unlike_post(request, name):
    return HttpResponseRedirect(reverse("index"))

def like_post(request, id):
    return 201

def unlike(request, id):
    return HttpResponseRedirect(reverse("index"))

def share(request, id):
    return 201



def search_view(request, query):
    return 200


def comment_post(request, id):
    return 201

def reply_comment(request, id):
    return 201


def delete_comment(request, id):
    return 201

def post_view(request, id):
    return 200

def notifications_view(request, id):
    return 200

def delete_post(request, id):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    post = Posts.objects.get(id = id)
    post.delete()

    return HttpResponseRedirect(reverse("index"))

def edit_post(request, id):
    return HttpResponseRedirect(reverse("index"))