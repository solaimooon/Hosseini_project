from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
import requests
import random
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *


def Register_view(request):
    sign_up_form_object = RegisterForm(request.POST)
    if sign_up_form_object.is_valid():
        # if the form valid , get username,passwoerd and redirect to verification view
        global phone_number
        phone_number = sign_up_form_object.cleaned_data["phone_number"]
        global password
        password = sign_up_form_object.cleaned_data["password1"]
        global first_name
        first_name = sign_up_form_object.cleaned_data["first_name"]
        global last_name
        last_name = sign_up_form_object.cleaned_data["last_name"]
        return HttpResponsePermanentRedirect(reverse("my_profile:Authentication"))
    else:
        for field, errors in sign_up_form_object.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
        return HttpResponsePermanentRedirect(reverse("website:index"))


def Authentication(request):
    if request.method == 'GET':
        # create the random codde between 1001 until 9999 and define it global to use all over the fanction
        global verification_code
        # creat the random number between the range give it
        verification_code = random.randint(1001, 9999)
        print(verification_code)
        key = '78634F47647561304B41467244444B344B7172625A73766939754C5644654376777A44726D6E6476517A383D'
        # this is the api of cavenegar , pass the key to url
        api = 'https://api.kavenegar.com/v1/%s/verify/lookup.json' % key
        # data must be send to api
        paloyd = {'receptor': str(phone_number), 'token': str(verification_code), "template": "verifyy"}
        #request to kavenegar to send massage
        response = requests.post(api, data=paloyd)
        return render(request, 'verification.html')
    elif request.method == 'POST':
        # get the numbers
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        number3 = request.POST.get('number3')
        number4 = request.POST.get('number4')
        # concat the numbers together
        number = int(number1 + number2 + number3 + number4)
        # validate the user insert the cerect valodation code
        if number == verification_code:
            # create user
            My_user_object = My_user.objects.create_user(phone_number=phone_number, password=password,
                                                         first_name=first_name, last_name=last_name)
            login(request, My_user_object)
            messages.add_message(request, messages.SUCCESS, "ثبت نام با موفقیت انجام شد")
            return HttpResponsePermanentRedirect(reverse("website:index"))


def log_in_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            print(form.errors)
            user = form.get_user()
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید.')
            # بازگشت به صفحه قبلی یا خانه
            #next_url = request.GET.get('next') or 'home'
            #return redirect(next_url)
            return HttpResponsePermanentRedirect(reverse('website:index'))

        else:
            print("سلام",form.errors)
            messages.error(request, 'نام کاربری یا رمز عبور نادرست است.')
            return HttpResponsePermanentRedirect(reverse('website:index'))
    else:
        return HttpResponsePermanentRedirect(reverse('website:index'))


def log_out_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("website:index"))


def profile_view(request):
    return render(request,'my-profile.html')
# Create your views here.
