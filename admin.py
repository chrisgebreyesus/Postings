from django.contrib import admin
from .models import Post, Condition, Category

class ConditionAdmin(admin.ModelAdmin):
    fields = ('condition_description',)
    list_display = ('condition_description',)
    search_fields = ('condition_description',)

admin.site.register(Condition, ConditionAdmin)
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    fields = ('category', 'post_description', 'condition', 'asking_price', 'email',) 
    list_display = ('post_description', 'format_asking_price' , 'category', 'condition', 'email', 'date_posted', )
    search_fields = ('post_description',)
    list_filter = ('date_posted', 'condition', 'category',)

admin.site.register(Post, PostAdmin)