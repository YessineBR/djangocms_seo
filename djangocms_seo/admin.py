from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from django.utils.translation import gettext_lazy as _

from .models import (
    MetaTag,
    OpenGraphMeta,
    TwitterCardMeta,
    SeoExtension,
    SeoExtensionMetaTag,
    SeoExtensionOpenGraphMeta,
    SeoExtensionTwitterMeta,
)
from .forms import MetaTagInlineForm, OpenGraphMetaTagInlineForm, TwitterMetaTagInlineForm


@admin.register(MetaTag)
class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    search_fields = ('name', 'content')
    list_filter = ('name',)


@admin.register(OpenGraphMeta)
class OpenGraphMetaAdmin(admin.ModelAdmin):
    list_display = ('property', 'content')
    search_fields = ('property', 'content')
    list_filter = ('property',)


@admin.register(TwitterCardMeta)
class TwitterCardMetaAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    search_fields = ('name', 'content')
    list_filter = ('name',)


class SeoExtensionMetaTagInline(admin.TabularInline):
    model = SeoExtensionMetaTag
    extra = 1
    verbose_name = _("Meta Tag Relationship")
    verbose_name_plural = _("Meta Tag Relationships")


class SeoExtensionOpenGraphMetaInline(admin.TabularInline):
    model = SeoExtensionOpenGraphMeta
    extra = 1
    verbose_name = _("Open Graph Relationship")
    verbose_name_plural = _("Open Graph Relationships")


class SeoExtensionTwitterMetaInline(admin.TabularInline):
    model = SeoExtensionTwitterMeta
    extra = 1
    verbose_name = _("Twitter Meta Relationship")
    verbose_name_plural = _("Twitter Meta Relationships")


class SeoExtensionAdmin(PageExtensionAdmin):
    inlines = [
        SeoExtensionMetaTagInline,
        SeoExtensionOpenGraphMetaInline,
        SeoExtensionTwitterMetaInline,
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('extended_object')


admin.site.register(SeoExtension, SeoExtensionAdmin)
