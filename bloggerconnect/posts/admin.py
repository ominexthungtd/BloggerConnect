from django.contrib import admin

# Register your models here.
from .models import Review, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user.profile)

    def has_change_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.owner == request.user.profile
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.owner == request.user.profile
        return super().has_delete_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user.profile
        obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Review)
admin.site.register(Tag)
