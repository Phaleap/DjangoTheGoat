from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class CarouselSlide(models.Model):
    is_active = models.BooleanField(default=False, help_text="Check this for the first slide to be 'active'.")
    headline = models.CharField(max_length=255, verbose_name="H1 Headline")
    description = models.TextField(verbose_name="Paragraph Text")
    image = models.ImageField(
        upload_to='images/carousel/',
        verbose_name="Slide Image (1920x800 recommended)",
        null=True,
        blank=True
    )
    
    button_text = models.CharField(max_length=50, default="VISIT SHOWROOM")
    button_link = models.URLField(default="#")
    
    order = models.IntegerField(default=0, help_text="Lower numbers appear first.")
    
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Carousel Slide"
        verbose_name_plural = "Carousel Slides"

    def __str__(self):
        return self.headline


class AboutHeroImages(models.Model):

    name = models.CharField(
        max_length=50,
        default="About Section Images & Text",
        unique=True,
        editable=False
    )
    image_main = models.ImageField(
        upload_to='images/about_hero/',
        verbose_name="Main Image (about_h1l1)",
        null=True,
        blank=True
    )

    image_overlay = models.ImageField(
        upload_to='images/about_hero/',
        verbose_name="Overlay Image (about_h1l2)",
        null=True,
        blank=True
    )

    tagline = models.CharField(
        max_length=100,
        default="ABOUT US",
        verbose_name="H5 Tagline (e.g., ABOUT US)"
    )

    title = models.CharField(
        max_length=255,
        verbose_name="H1 Title (e.g., Creative solutions...)",
        help_text="Use <br> for line breaks."
    )

    content = models.TextField(
        verbose_name="Paragraph Content",
        help_text="The main description paragraph."
    )

    button_text = models.CharField(
        max_length=50,
        default="CONTINUE READING",
        verbose_name="Button Text"
    )

    # ===== NEW: OUR STORY SECTION =====
    story_image = models.ImageField(
        upload_to='images/about_story/',
        verbose_name="Our Story Image",
        null=True,
        blank=True
    )

    story_small_title = models.CharField(
        max_length=100,
        default="Our Story",
        verbose_name="Our Story Small Title (H5)"
    )

    story_main_title = models.CharField(
        max_length=255,
        default="Crafting Comfort For Every Home",
        verbose_name="Our Story Main Title (H2)"
    )

    story_paragraph_1 = models.TextField(
    blank=True,
    verbose_name="Our Story Paragraph 1"
)

    story_paragraph_2 = models.TextField(
    blank=True,
    verbose_name="Our Story Paragraph 2"
)

    class Meta:
        verbose_name = "About Section Image & Text"
        verbose_name_plural = "About Section Image & Text"

    def __str__(self):
        return self.name


class ProjectSectionHeader(models.Model):
    name = models.CharField(max_length=50, default="Project Section Header", unique=True, editable=False)
    tagline = models.CharField(
        max_length=100, 
        default="OUR PROJECT", 
        verbose_name="H6 Tagline (e.g., OUR PROJECT)"
    )
    title = models.CharField(
        max_length=255, 
        default="Explore our kitchen designs",
        verbose_name="H1 Title"
    )
    content = models.TextField(
        verbose_name="Paragraph Content",
        help_text="The main description paragraph. Use <br> for line breaks."
    )

    class Meta:
        verbose_name = "Project Section Header Text"
        verbose_name_plural = "Project Section Header Text"

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(
        max_length=150, 
        verbose_name="Project Title (e.g., Kitchen project 01)"
    )
    image = models.ImageField(
        upload_to='images/projects/',
        verbose_name="Project Image",
    )
    categories = models.CharField(
        max_length=255,
        help_text="Enter categories separated by commas (e.g., Modern, Coastal, Top Sellers)"
    )
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['id'] # Ensure projects are retrieved in a consistent order

    def get_categories_list(self):
        """Returns a list of categories for easier template iteration."""
        return [c.strip() for c in self.categories.split(',')]

    def __str__(self):
        return self.title

class TeamSectionHeader(models.Model):
    name = models.CharField(max_length=50, default="Team Section Header", unique=True, editable=False)
    tagline = models.CharField(
        max_length=100, 
        default="MEET OUR TEAM", 
        verbose_name="H6 Tagline (e.g., MEET OUR TEAM)"
    )
    title = models.CharField(
        max_length=255, 
        default="Creative minds always <br> think someting",
        verbose_name="H1 Title",
        help_text="Use <br> for line breaks."
    )

    class Meta:
        verbose_name = "Team Section Header Text"
        verbose_name_plural = "Team Section Header Text"

    def __str__(self):
        return self.name

    
class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    def __str__(self):         
        return self.categoryName
    
class Product(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    productDescript = RichTextUploadingField(null=True)
    availability = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='images/Products/', null=True, blank=True)

    rating = models.FloatField(default=0)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.productName} - {self.categoryID.categoryName}'
    
class ProductDetail(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Description =  RichTextUploadingField(null=True)
    Information = RichTextUploadingField(null=True)
    Reviews = RichTextUploadingField(null=True)
    def __str__(self):         
        return f'{self.id} - {self.productID.productName}'
    

    
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    facebook = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    about_short = models.TextField(blank=True, null=True)
    about_long = models.TextField(blank=True, null=True)

    honors = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)

    skill_1_name = models.CharField(max_length=50, blank=True, null=True)
    skill_1_value = models.IntegerField(blank=True, null=True)

    skill_2_name = models.CharField(max_length=50, blank=True, null=True)
    skill_2_value = models.IntegerField(blank=True, null=True)

    skill_3_name = models.CharField(max_length=50, blank=True, null=True)
    skill_3_value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class TestimonialClient(models.Model):
    client_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, verbose_name="Client Role/Designation")
    quote = models.TextField()
    image = models.ImageField(
        upload_to='images/testimonials/',
        verbose_name="Client Image (e.g. 100x100 recommended)"
    )
    
    # Use this to group testimonials into slides of 3
    slide_group = models.IntegerField(default=1, help_text="Group number for the carousel slide (e.g., 1 for slide 1, 2 for slide 2, etc.)")
    
    order_in_group = models.IntegerField(default=1, help_text="Position within the slide group (1, 2, or 3)")

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['slide_group', 'order_in_group']

    def __str__(self):
        return f"{self.client_name} (Group {self.slide_group})"    
    
class BlogCategory(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True)

  class Meta:
    verbose_name_plural = "Blog Categories"
    
  def __str__(self):
    return self.name

class BlogTag(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True)

  def __str__(self):
    return self.name
  
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text="A unique, URL-friendly version of the title.")
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(BlogTag, blank=True)
    image = models.ImageField(
        upload_to='images/blog/',
        verbose_name="Blog Post Image"
    )
    author = models.CharField(
        max_length=100, 
        default="Admin"
    )
    # Using RichTextUploadingField for the main body content
    content = RichTextUploadingField(verbose_name="Full Blog Content")
    
    # Short summary for the index page card
    summary = models.TextField(
        max_length=300, 
        help_text="A brief summary for the homepage card."
    )
    
    # Assuming comments will be a separate feature, but we can store the count if needed
    comment_count = models.IntegerField(default=0)
    
    # Store the publish date
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-published_date']

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'id': self.id})  
class BillingDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    qr_code_image = models.ImageField(upload_to='qrcodes/', null=True, blank=True)
    total = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
class QRCode(models.Model):
    # Field to store the QR code image file
    qr_image = models.ImageField(upload_to='qrcodes/', verbose_name="QR Code Image")
    # Field for a payment method name (optional but recommended)
    name = models.CharField(max_length=100, default="Payment Method") 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (Active: {self.is_active})"


class WhatWeOffer(models.Model):
    name = models.CharField(
        max_length=50,
        default="What We Offer Section",
        unique=True,
        editable=False
    )

    small_title = models.CharField(
        max_length=100,
        default="What We Offer?"
    )

    main_title = models.CharField(
        max_length=255,
        default="Our Company Make You Feel More Confident"
    )

    description_1 = models.TextField(
        help_text="First description paragraph"
    )

    description_2 = models.TextField(
        help_text="Second description paragraph"
    )

    # Feature list
    feature_1 = models.CharField(max_length=100, default="Best Sofa")
    feature_2 = models.CharField(max_length=100, default="Best Quality")
    feature_3 = models.CharField(max_length=100, default="Good Prices")
    feature_4 = models.CharField(max_length=100, default="Fast Delivery")

    image = models.ImageField(
        upload_to="images/what_we_offer/",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "What We Offer Section"
        verbose_name_plural = "What We Offer Section"

    def __str__(self):
        return self.name
