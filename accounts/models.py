from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

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

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField # Keep this if needed for other models

# ... (Existing models)

class AboutHeroImages(models.Model):
    # This ensures only one entry can exist in the admin
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
    
    # --- New Text Fields ---
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
    
    # Optional: For the button at the bottom of the text block
    button_text = models.CharField(
        max_length=50, 
        default="CONTINUE READING", 
        verbose_name="Button Text"
    )
    # The button link already uses {% url 'aboutFur' %}, so we don't need a field for it unless the destination changes.

    class Meta:
        verbose_name = "About Section Image & Text"
        verbose_name_plural = "About Section Image & Text"

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
    availability = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='images/Products/',null=True,blank=True)
    productDate = models.DateTimeField(auto_now_add=True, null=True)
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

        