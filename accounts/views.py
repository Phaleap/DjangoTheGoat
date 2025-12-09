from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from accounts.models import *
from .models import BlogCategory, BlogTag
from django.core.paginator import Paginator
from django.db.models import Count, Q  # Q needed for advanced filtering/searching if implemented

# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def indexFur(request):
    slides = CarouselSlide.objects.all() 
    about_images = AboutHeroImages.objects.first() 
    project_header = ProjectSectionHeader.objects.first()
    projects = Project.objects.all()
    team_header = TeamSectionHeader.objects.first()
    team_members = TeamMember.objects.all()
    
    # --- Testimonial Logic ---
    testimonials = TestimonialClient.objects.all()
    slide_groups = testimonials.values_list('slide_group', flat=True).distinct()
    testimonial_slides = []
    for group_id in slide_groups:
        slide_testimonials = testimonials.filter(slide_group=group_id)
        testimonial_slides.append(list(slide_testimonials[:3]))
    # --- End Testimonial Logic ---

    latest_posts = BlogPost.objects.all()[:3]

    context = {
        'slides': slides,
        'about_images': about_images,
        'project_header': project_header,
        'projects': projects,
        'team_header': team_header, 
        'team_members': team_members,
        'testimonial_slides': testimonial_slides,
        'latest_posts': latest_posts,
    }
    return render(request, 'furniture/index.html', context)

def aboutFur(request):
    return render(request, 'furniture/about.html')

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)

    # Recent posts (excluding the current one)
    recent_posts = BlogPost.objects.exclude(id=post.id).order_by('-published_date')[:3]

    related_posts = BlogPost.objects.filter(
        category=post.category
    ).exclude(
        id=post.id
    ).order_by('-published_date')[:2]

    categories = BlogCategory.objects.annotate(
        post_count=Count('blogpost')
    ).filter(post_count__gt=0)

    tags = BlogTag.objects.all()

    context = {
        'post': post,
        'recent_posts': recent_posts,     # <<< IMPORTANT
        'related_posts': related_posts,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'furniture/blog_detail.html', context)



# ----------------------------------------------------
# 🌟 NEW: Blog Category View (Fixes the blogCategory error)
# ----------------------------------------------------
def blogCategory(request, slug):
    category = get_object_or_404(BlogCategory, slug=slug)
    post_list = BlogPost.objects.filter(category=category).order_by('-published_date')
    
    # Reusing the logic from blog_list_view for the sidebar
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    recent_posts = BlogPost.objects.order_by('-published_date')[:3]
    category_counts = BlogCategory.objects.annotate(count=Count('blogpost')).filter(count__gt=0)
    categories_with_count = {cat.name: cat.count for cat in category_counts}
    tags = BlogTag.objects.annotate(count=Count('blogpost')).order_by('-count')[:8]
    gallery_images = BlogPost.objects.all()[:6]

    context = {
        'posts': posts,
        'current_category': category,
        'recent_posts': recent_posts,
        'categories_with_count': categories_with_count,
        'tags': tags,
        'gallery_images': gallery_images,
    }
    return render(request, 'furniture/blog.html', context)
# ----------------------------------------------------

# ----------------------------------------------------
# 🌟 NEW: Blog Tag View (Fixes the blogTag error)
# ----------------------------------------------------
def blogTag(request, slug):
    tag = get_object_or_404(BlogTag, slug=slug)
    # Filter posts where the tags M2M field contains the current tag
    post_list = BlogPost.objects.filter(tags=tag).order_by('-published_date')
    
    # Reusing the logic from blog_list_view for the sidebar
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    recent_posts = BlogPost.objects.order_by('-published_date')[:3]
    category_counts = BlogCategory.objects.annotate(count=Count('blogpost')).filter(count__gt=0)
    categories_with_count = {cat.name: cat.count for cat in category_counts}
    tags_sidebar = BlogTag.objects.annotate(count=Count('blogpost')).order_by('-count')[:8]
    gallery_images = BlogPost.objects.all()[:6]

    context = {
        'posts': posts,
        'current_tag': tag,
        'recent_posts': recent_posts,
        'categories_with_count': categories_with_count,
        'tags': tags_sidebar, # Using tags_sidebar to avoid conflict with 'current_tag'
        'gallery_images': gallery_images,
    }
    return render(request, 'furniture/blog.html', context)
# ----------------------------------------------------

def blog_list_view(request):
    query = request.GET.get('q')  # Get the search text

    if query:
        all_posts = BlogPost.objects.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-published_date')
    else:
        all_posts = BlogPost.objects.all().order_by('-published_date')

    # Pagination (still applied after search)
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    # Recent posts (not filtered by search)
    recent_posts = BlogPost.objects.order_by('-published_date')[:3]

    # Categories with count
    category_counts = BlogCategory.objects.annotate(count=Count('blogpost')).filter(count__gt=0)
    categories_with_count = {
        cat.name: {'count': cat.count, 'slug': cat.slug} for cat in category_counts
    }

    # Tags with count
    tags = BlogTag.objects.annotate(count=Count('blogpost')).order_by('-count')[:8]

    # Gallery (latest 6)
    gallery_images = BlogPost.objects.all()[:6]

    context = {
        'posts': posts,
        'recent_posts': recent_posts,
        'categories_with_count': categories_with_count,
        'tags': tags,
        'gallery_images': gallery_images,
        'query': query,
    }
    return render(request, 'furniture/blog.html', context)
    
def blog(request):
    return blog_list_view(request) 


def cart(request):
    return render(request, 'furniture/cart.html')

def checkOut(request):
    return render(request, 'furniture/checkout.html')

def contact(request):
    return render(request, 'furniture/contact.html')

def detail(request, id): 
    product = Product.objects.get(id=id)
    detail = ProductDetail.objects.filter(productID=product).first()
    images = ProductDetailImage.objects.filter(productID=product)

    context = {
        "product": product,
        "detail": detail,
        "images": images,
    }
    return render(request, 'furniture/detail.html', context)

def pricing(request):
    return render(request, 'furniture/pricing.html')

def shop(request):
    DTproducts = Product.objects.all()
    DTCategory = Category.objects.all()
    bestsellers = Product.objects.filter(is_bestseller=True)[:3]
    context = {
    'Objproducts': DTproducts,
    'ObjDTCategory': DTCategory,
    'bestsellers': bestsellers,
}
    return render(request, 'furniture/shop.html', context)

def team(request):
    DTmembers = TeamMembers.objects.all()
    context = {
        "objDTmembers": DTmembers,
    }
    return render(request, 'furniture/team.html', context)


def team_detail(request, id):
    member = get_object_or_404(TeamMembers, id=id)

    social_links = []
    if member.facebook:
        social_links.append({"url": member.facebook, "icon": "fab fa-facebook"})
    if member.telegram:
        social_links.append({"url": member.telegram, "icon": "fab fa-telegram-plane"})
    if member.youtube:
        social_links.append({"url": member.youtube, "icon": "fab fa-youtube"})

    skills = []
    if member.skill_1_name and member.skill_1_value is not None:
        skills.append({"name": member.skill_1_name, "percent": member.skill_1_value})
    if member.skill_2_name and member.skill_2_value is not None:
        skills.append({"name": member.skill_2_name, "percent": member.skill_2_value})
    if member.skill_3_name and member.skill_3_value is not None:
        skills.append({"name": member.skill_3_name, "percent": member.skill_3_value})
    
    context = {
        "member": member,
        "social_links": social_links,
        "skills": skills,
    }

    return render(request, 'furniture/team_detail.html', context)