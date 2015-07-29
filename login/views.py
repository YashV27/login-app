from django.http import HttpResponse

from login.models import User

def index(request):
    return HttpResponse("Login")
    user_list = User.objects.get()

    username = ""
    password = ""


def signup(request):
    return HttpResponse("Signup")
    
def edit_profile(request,user_id):
    return HttpResponse("Edit your profile")
    
def profile(request,user_id):
    return HttpResponse("Your Profile")
    
def change_password(request,user_id):
    return HttpResponse("Change your password")
