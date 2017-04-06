from django.contrib import admin
from .models import Area, Category, LandNum, Owner, LandOwner


class InlineAreaLandNum(admin.TabularInline):
    model = LandNum
    # raw_id_fields = ('area',)


class InlineOwnerLandNum(admin.TabularInline):
    model = Owner
#     fk_name = 'Owner'
    # raw_id_fields = ('owner',)


# class InlineOwner(admin.TabularInline):
#     model = Owner
#     fk_name = 'owner'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']
    search_fields = ['name', 'desc']
    inlines = [InlineAreaLandNum]


@admin.register(LandOwner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = []
    # pass

@admin.register(LandNum)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [InlineOwnerLandNum]