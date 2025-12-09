from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.

class CarouselSlide(models.Model):
    # Field to track if this slide is the active one (the first one)
    is_active = models.BooleanField(default=False, help_text="Check this for the first slide to be 'active'.")
    
    # Text content
    headline = models.CharField(max_length=255, verbose_name="H1 Headline")
    description = models.TextField(verbose_name="Paragraph Text")
    
    # Image upload
    image = models.ImageField(
        upload_to='images/carousel/',
        verbose_name="Slide Image (1920x800 recommended)",
        null=True,
        blank=True
    )
    
    # Optional: Button link/text (based on your template)
    button_text = models.CharField(max_length=50, default="VISIT SHOWROOM")
    button_link = models.URLField(default="#")
    
    # Ordering field to control the display order
    order = models.IntegerField(default=0, help_text="Lower numbers appear first.")
    
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Carousel Slide"
        verbose_name_plural = "Carousel Slides"

    def __str__(self):
        return self.headline

# accounts/models.py

class AboutHeroImages(models.Model):

    name = models.CharField(max_length=50, default="About Section Images & Text", unique=True, editable=False)
    
    # --- Existing Image Fields ---
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
    
    # Optional: If you have a separate Detail page for each project
    # project_url = models.URLField(max_length=200, blank=True, null=True) 

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

class TeamMember(models.Model):
    name = models.CharField(
        max_length=150, 
        verbose_name="Member Name"
    )
    designation = models.CharField(
        max_length=100, 
        verbose_name="Designation (Role, e.g., Designer, Architect)"
    )
    image = models.ImageField(
        upload_to='images/team_members/',
        verbose_name="Member Image",
    )

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['id']

    def __str__(self):
        return self.name
    
class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    categoryImage = models.ImageField(upload_to='images/Categories/',null=True,blank=True)
    def __str__(self):         
        return self.categoryName
    
class Product(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=200, null=True)
    productDescript =  RichTextUploadingField(null=True)
    is_bestseller = models.BooleanField(default=False)
    availability = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='images/Products/',null=True,blank=True)
    productDate = models.DateTimeField(auto_now_add=True, null=True)
    is_bestseller = models.BooleanField(default=False)
    def __str__(self):         
        return f'{self.id} - {self.productName} - {self.categoryID.categoryName}'
class ProductDetail(models.Model):
    productDetailName = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Description =  RichTextUploadingField(null=True)
    Information = RichTextUploadingField(null=True)
    Reviews = RichTextUploadingField(null=True)
    productDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    def __str__(self):         
        return f'{self.id} - {self.productDetailName} - {self.productID.productName}'
    
class ProductDetailImage(models.Model):
    productDetailImageName = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    productDetailImage = models.ImageField(upload_to='images/productDetail/',null=True,blank=True)
    imageDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
       return f'{self.id} - {self.productDetailImageName} - {self.productID.productName}'

# Ozai Team and Team Detail 
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
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
        # Assuming you will map this to a blog detail page
        return f"/blog/{self.slug}/"    
