# accounts/admin.py

from django.contrib import admin
from accounts.models import *
from .models import QRCode 
from django.utils.html import format_html

# Product & other models

class ProductAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.productImage:
            return format_html('<img src="{}" width="100" />', obj.productImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    list_display = ["image_preview","productName","price","categoryID","availability" ]
    list_filter = ["categoryID","availability"]
    search_fields = ["productName"]
    list_per_page = 6
    readonly_fields = ["image_preview"]


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
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
admin.site.register(ContactMessage)
admin.site.register(BillingDetail)

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'qr_image', 'is_active')   # Columns to show
    list_editable = ('is_active',)                   # Toggle active in list view
    list_filter = ('is_active',)       

class AboutHeroImagesAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Hero Section", {
            "fields": (
                "image_main",
                "image_overlay",
                "tagline",
                "title",
                "content",
                "button_text",
            )
        }),
        ("Our Story Section", {
            "fields": (
                "story_image",
                "story_small_title",
                "story_main_title",
                "story_paragraph_1",
                "story_paragraph_2",
            )
        }),
    )

@admin.register(WhatWeOffer)
class WhatWeOfferAdmin(admin.ModelAdmin):
    list_display = ("name", "small_title", "main_title")


