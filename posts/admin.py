from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'title', 'photo', 'created', 'modified')
    list_editable = ('title', 'title',)

    search_fields = ('user__username', 'created',)

    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified',)

    fieldsets = (
        ('Date post', {
            'fields': (
                ('user', 'profile',),
                ('title', 'photo',),
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified',),
            ),
        }),
    )

    readonly_fields = ('created', 'modified')
