from django.contrib import admin

from app.models import Article, Promo, Client, Document


class DocumentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fields = ('file',)


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article)
admin.site.register(Promo)
admin.site.register(Client, ClientAdmin)
admin.site.register(Document, DocumentAdmin)
