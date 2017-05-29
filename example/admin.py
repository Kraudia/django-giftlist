from django.contrib import admin

# Register your models here.
from django.contrib import admin
from example.models import GiftList, Gift


class GiftInLine(admin.TabularInline):
    model = Gift
    extra = 1


class GiftListAdmin(admin.ModelAdmin):
    inlines = (GiftInLine, )

admin.site.register(GiftList, GiftListAdmin)
admin.site.register(Gift)