from django.contrib import admin
from .models import User, Membership, Members


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',
                    'phone_number', 'gym_name', 'gym_location', 'gym_phone')


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_type',
                    'membership_duration', 'membership_price')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number',
                    'age', 'gender', 'address', 'membership', 'validity')


admin.site.register(User, UserAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Members, MemberAdmin)
