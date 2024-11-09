from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_http_methods(["GET", "POST"])
def index(request):
    return HttpResponse("Hello, world. You're at the attendance index.")

@require_http_methods(["POST"])
@login_required
def new_user(request:HttpRequest):
    if not request.user.groups:
        return HttpResponseForbidden("You don't have perms")
    request.user.user_permissions
    request.POST
    User.objects.create_user(username, "lennon@thebeatles.com", "johnpassword")