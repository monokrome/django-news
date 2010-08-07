from django.contrib import admin
from models import Article

# Add this back when we make attachments support optional
# from attachments.admin import AttachmentInlines

class ArticleAdmin(admin.ModelAdmin):
#    inlines = [AttachmentInlines]
    list_display = ('title','published','created_on','markup_filter','slug')

    fieldsets = (
        ('Article Information', {'fields': ('title','body','published')}),
        ('Advanced', {
            'fields': ['markup_filter', 'author','slug','created_on','summary',],
            'classes': ['collapse',],
        }),
    )

admin.site.register(Article, ArticleAdmin)
