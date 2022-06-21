import re
from tkinter import Widget
from attr import attr
from django import forms
from django.db import IntegrityError
from django.forms import EmailInput, ModelForm, TextInput
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

import json
from .models import User, Membership, Members
from .forms import MembershipForm, UserForm, MemberForm, SearchForm


def index(request):
    return render(request, 'Membership/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'Membership/login.html',
                          {'message': 'Invalid username and password'})

    return render(request, 'Membership/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    template = 'Membership/register.html'
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        personal_address = request.POST['personal_address']
        date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        gym_name = request.POST['gym_name']
        gym_location = request.POST['gym_location']
        gym_phone = request.POST['gym_phone']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, template, {'message': 'Passwords do not match'})

        try:
            user = User(username=username, first_name=first_name, last_name=last_name, email=email, personal_address=personal_address,
                        date_of_birth=date_of_birth, phone_number=phone_number, gender=gender, gym_name=gym_name, gym_location=gym_location, gym_phone=gym_phone)
            user.set_password(password)
            user.save()
        except IntegrityError:
            return render(request, template, {
                'message': "Email already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    return render(request, template, {'form': UserForm()})


def membership(request):
    template = 'Membership/membership.html'
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            mem_type = form.cleaned_data['membership_type']
            mem_duration = form.cleaned_data['membership_duration']
            mem_price = form.cleaned_data['membership_price']

            membership = Membership(user=request.user, membership_type=mem_type,
                                    membership_duration=mem_duration, membership_price=mem_price)
            membership.save()

            return render(request, template, {
                'message': 'Successfully Added Membership Plan',
                'form': MembershipForm()
            })

    return render(request, template, {
        'form': MembershipForm()
    })


def add_members(request):
    template = 'Membership/add-members.html'
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            membership = form.cleaned_data['membership']
            validity = form.cleaned_data['validity']

            member = Members(gym_owner=request.user, first_name=first_name, last_name=last_name, email=email,
                             phone_number=phone_number, age=age, gender=gender, address=address, membership=membership, validity=validity)
            member.save()

            return render(request, template, {
                'message': 'Successfully Added Member into the Gym',
                'form': MemberForm()
            })

    return render(request, template, {
        'form': MemberForm()
    })


def all_members(request):
    members = Members.objects.filter(
        gym_owner=request.user).order_by('validity').all()
    paginator = Paginator(members, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'Membership/all-members.html', {
        'page_obj': page_obj,
        'form': SearchForm()
    })


def member_search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['search']
        search_member = Members.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        ).order_by('validity').all()

        return render(request, 'Membership/member-search-results.html', {
            'search_results': search_member
        })


def member_detail(request, id):
    template = "Membership/member-detail.html"
    member = Members.objects.get(pk=id)
    return render(request, template, {
        'member': member
    })


@login_required
def edit(request):
    if request.method != 'POST':
        JsonResponse({'error': 'Invalid request'})

    data = json.loads(request.body)
    id = data.get('id','')
    email = data.get('email', '')
    age = data.get('age', '')
    phone_number = data.get('phone', '')
    address = data.get('address', '')

    member = Members.objects.get(pk=id)
    member.email = email
    member.age = age
    member.phone_number = phone_number
    member.address = address
    member.save()

    return HttpResponseRedirect(reverse('member-detail', args=(id,)))
