from django.contrib import admin
from .models import *
class RequestTimeslotAdminInline(admin.TabularInline):
    model = RequestTimeslot

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    inlines = (RequestTimeslotAdminInline, )

    pass

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    pass
@admin.register(Tutee)
class TuteeAdmin(admin.ModelAdmin):
    pass
@admin.register(RequestTimeslot)
class RequestTimeslotAdmin(admin.ModelAdmin):
    pass
@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    pass
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
@admin.register(TransactionTable)
class TransactionTable(admin.ModelAdmin):
    pass
