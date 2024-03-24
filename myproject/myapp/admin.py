from django.contrib import admin
from django.utils.html import format_html
from . models import Student, Category, Item



admin.site.site_header='My WebSite'
admin.site.site_title='Administration'
admin.site.index_title='My WebSite'
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','email_id','city')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('cat_name','cat_desc')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def item_image(self, obj):
        return format_html('<img src="{}" width="60" height="60">'.format(obj.i_imgage.url))
    list_display=('i_name', 'i_price', 'i_desc', 'category', 'item_image')
