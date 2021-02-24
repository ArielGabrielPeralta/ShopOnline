from django.contrib import admin

from OrderManage.models import Costumers, Article, Orders

# Register your models here.


class CostumerAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone")
    search_fields = ("name", "phone")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "price")
    list_filter = ('section',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'date')
    list_filter = ('date',)
    date_hierarchy = 'date'


admin.site.register(Costumers, CostumerAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Orders, OrderAdmin)
