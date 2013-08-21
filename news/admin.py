from django.contrib import admin
from .models import Reporter, Article

#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']

#class ChoiceInline(admin.StackedInline):
#class ChoiceInline(admin.TabularInline):
#    model = Reporter
#    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['headline']}),
        ('Published date', {'fields': ['pub_date'], }),# 'classes': ['collapse']
        ('Reporter', {'fields': ['reporter'],}),
    ]
    #inlines = [ChoiceInline]
    list_display = ('headline', 'pub_date', 'reporter')
    list_filter = ['pub_date']
    search_fields = ['headline']
    date_hierarchy = 'pub_date'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Reporter)