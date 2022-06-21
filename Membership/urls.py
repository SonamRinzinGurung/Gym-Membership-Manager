from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path("login",views.login_view, name='login'),
    path("logout",views.logout_view, name='logout'),
    path("register",views.register, name='register'),
    path("membership",views.membership, name='membership'),
    path("add-members",views.add_members, name='add-members'),
    path("all-members",views.all_members, name='all-members'),
    path("member-search", views.member_search, name='member-search'),
    path("member/<int:id>", views.member_detail, name='member-detail'),
    path("edit", views.edit, name='edit'),
]