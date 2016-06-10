from django.contrib import admin

from app.models import Article, Promo, Client, Document


class DocumentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fields = ('file_en', 'file_ru',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordering')
    list_editable = ('ordering',)


class PromoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Document, DocumentAdmin)
