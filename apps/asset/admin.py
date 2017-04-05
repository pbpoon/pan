from django.contrib import admin
from django import forms
from .models import Area, Category, LandNum, Owner


class InlineAreaLandNum(admin.TabularInline):
    model = LandNum
    # raw_id_fields = ('area',)


class InlineOwnerLandNum(admin.TabularInline):
    model = Owner
    # raw_id_fields = ('owner',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']
    search_fields = ['name', 'desc']
    inlines = [InlineAreaLandNum]


@admin.register(LandNum)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [InlineOwnerLandNum]