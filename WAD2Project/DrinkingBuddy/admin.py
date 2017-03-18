from django.contrib import admin
from DrinkingBuddy.models import Page, UserProfile, Comment

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	
class CommentAdmin(admin.ModelAdmin):
	list_display = ('comment', 'commenter', 'page', 'date')

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment, CommentAdmin)