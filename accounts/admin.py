# accounts/admin.py

from django.contrib import admin
from accounts.models import *

# Product & other models
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(CarouselSlide)
admin.site.register(AboutHeroImages)
admin.site.register(ProjectSectionHeader)
admin.site.register(Project)
admin.site.register(TeamSectionHeader)
admin.site.register(TeamMembers)
admin.site.register(TestimonialClient)

# Blog models
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BlogTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogTag, BlogTagAdmin)
