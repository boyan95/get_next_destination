from django.contrib import admin
from steal_destination.main.models import Destination
from .models import Post, PostImage


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'type',)

    class Meta:
        model = Destination


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
