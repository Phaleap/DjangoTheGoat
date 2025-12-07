# accounts/admin.py

from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductDetailImage)

# Register the new CarouselSlide model
admin.site.register(CarouselSlide)
admin.site.register(AboutHeroImages)
admin.site.register(ProjectSectionHeader)
admin.site.register(Project)
admin.site.register(TeamSectionHeader)
admin.site.register(TeamMember)