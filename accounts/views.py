from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from accounts.models import *
from .models import BlogCategory, BlogTag
from django.core.paginator import Paginator
from django.db.models import Count, Q  # Q needed for advanced filtering/searching if implemented
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Product
import math
from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages
from .models import QRCode 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from decimal import Decimal
# Create your views here.



def indexFur(request):
    slides = CarouselSlide.objects.all() 
    about_images = AboutHeroImages.objects.first() 
    project_header = ProjectSectionHeader.objects.first()
    projects = Project.objects.all()
    team_header = TeamSectionHeader.objects.first()
    projects = Project.objects.all()
    projects_per_slide = 3
    grouped_projects = []
    for i in range(0, len(projects), projects_per_slide):
        grouped_projects.append(projects[i:i + projects_per_slide])
    testimonials = TestimonialClient.objects.all()
    slide_groups = testimonials.values_list('slide_group', flat=True).distinct()
    testimonial_slides = []
    for group_id in slide_groups:
        slide_testimonials = testimonials.filter(slide_group=group_id)
        testimonial_slides.append(list(slide_testimonials[:3]))
    projects = Project.objects.all()
    project_slide_count = math.ceil(projects.count() / 3)
    latest_posts = BlogPost.objects.all()[:3]

    context = {
        'slides': slides,
        'projects_slides': grouped_projects,
        'about_images': about_images,
        'project_header': project_header,
        'projects': projects,
        'project_slide_count': project_slide_count,
        'team_header': team_header, 
        'testimonial_slides': testimonial_slides,
        'latest_posts': latest_posts,
    }
    return render(request, 'furniture/index.html', context)

def aboutFur(request):
    about_images = AboutHeroImages.objects.first()
    what_we_offer = WhatWeOffer.objects.first()

    testimonials = TestimonialClient.objects.all()
    slide_groups = testimonials.values_list('slide_group', flat=True).distinct()
    testimonial_slides = []
    for group_id in slide_groups:
        slide_testimonials = testimonials.filter(slide_group=group_id)
        testimonial_slides.append(list(slide_testimonials[:3]))

    context = {
        'about_images': about_images,
        'what_we_offer': what_we_offer,
        'testimonial_slides': testimonial_slides,
    }

    return render(request, 'furniture/about.html', context)



def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
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
        'recent_posts': recent_posts,   
        'related_posts': related_posts,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'furniture/blog_detail.html', context)


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
    DTproduct = Product.objects.get(id=id)
    DTdetail = ProductDetail.objects.filter(productID=DTproduct).first()
    full_stars = range(int(DTproduct.rating))
    context = {
        "product": DTproduct,
        "detail": DTdetail,
        "full_stars": full_stars,
    }
    return render(request, 'furniture/detail.html', context)

def pricing(request):
    return render(request, 'furniture/pricing.html')


def shop(request, category_id=None):
    DTCategory = Category.objects.all()
    DTproducts = Product.objects.all()
    bestsellers = Product.objects.filter(is_bestseller=True)[:3]

    # CATEGORY FILTER
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        DTproducts = DTproducts.filter(categoryID=category)
    else:
        category = None

    # PRICE FILTER
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    if min_price:
        DTproducts = DTproducts.filter(price__gte=Decimal(min_price))
    if max_price:
        DTproducts = DTproducts.filter(price__lte=Decimal(max_price))

    # PAGINATION
    paginator = Paginator(DTproducts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'Objproducts': page_obj,
        'ObjDTCategory': DTCategory,
        'bestsellers': bestsellers,
        'category': category,
        'page_obj': page_obj,
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

def get_cart_data(request):
    cart_items = request.session.get('cart', {})
    cart_list = []
    total = 0
    count = 0

    for product_id, item_data in cart_items.items():
        try:
            product = Product.objects.get(id=int(product_id))
            quantity = item_data.get("qty", 1)
            price = float(item_data.get("price", product.price))

            # Safe image handling
            try:
                image_url = product.image.url
            except:
                try:
                    image_url = product.productImage.url
                except:
                    image_url = ""

            subtotal = price * quantity
            total += subtotal
            count += quantity
            
            cart_list.append({
                'id': product.id,
                'name': item_data.get("name", product.productName),
                'qty': quantity,
                'price': price,
                'image': image_url,
            })

        except Product.DoesNotExist:
            continue

    return {
        'count': count,
        'total': total,
        'items': cart_list
    }



@require_POST
def add_to_cart(request):
    try:
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        if not product_id or not quantity:
            return JsonResponse({'error': 'Missing product ID or quantity.'}, status=400)

        try:
            product_id = int(product_id)
            quantity = int(quantity)
        except ValueError:
            return JsonResponse({'error': 'Invalid ID or quantity format.'}, status=400)

        if quantity <= 0:
            return JsonResponse({'error': 'Quantity must be positive.'}, status=400)

        product = Product.objects.get(id=product_id)

        cart = request.session.get('cart', {})
        product_key = str(product_id)

        if product_key in cart:
            cart[product_key]['qty'] += quantity
        else:
            cart[product_key] = {
                'name': product.productName,
                'price': float(product.price),
                'qty': quantity,
                'image': product.productImage.url if product.productImage else ''
            }

        request.session['cart'] = cart
        request.session.modified = True

        cart_data = get_cart_data(request)
        return JsonResponse(cart_data)

    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found.'}, status=404)

    except Exception as e:
        print(f"Server Error in add_to_cart: {e}")
        return JsonResponse({'error': f'Internal Server Error: {str(e)}'}, status=500)

    
@require_POST
def remove_from_cart(request):
    try:
        product_id = request.POST.get('product_id')
        
        if not product_id:
            return JsonResponse({'error': 'Missing product ID.'}, status=400)
            
        product_key = str(product_id)
        cart = request.session.get('cart', {})
        
        # Check if the product is in the cart and remove it
        if product_key in cart:
            del cart[product_key]
            request.session['cart'] = cart
            request.session.modified = True
        
        # Return the updated cart data (count, total, and new item list)
        cart_data = get_cart_data(request)
        return JsonResponse(cart_data)

    except Exception as e:
        print(f"Server Error in remove_from_cart: {e}")
        return JsonResponse({'error': f'Internal Server Error: {str(e)}'}, status=500)
    
@login_required(login_url='login')
def billing_add(request):
    cart_data = get_cart_data(request)

    subtotal = cart_data['total']
    shipping = 20
    total = subtotal + shipping

    if request.method == "POST":
        data = request.POST
        qr_image = request.FILES.get('qr_code_image')

        billing = BillingDetail(
            first_name=data['first_name'],
            last_name=data['last_name'],
            country=data['country'],
            address=data['address'],
            town=data['town'],
            postcode=data['postcode'],
            phone=data['phone'],
            email=data['email'],
            qr_code_image=qr_image,
            total=total
        )
        billing.save()
        return redirect('BillingList')

    return render(request, 'furniture/checkout.html', {
        'items': cart_data['items'],  # <— list of items with id, name, price, qty
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    })

    cart = request.session.get('cart', {})

    # Calculate subtotal
    subtotal = sum(item["qty"] * float(item["price"]) for item in cart.values())

    # If you want to add shipping (example: $20)
    shipping = 20  
    total = subtotal + shipping

    if request.method == "POST":
        data = request.POST
        qr_image = request.FILES.get('qr_code_image')

        billing = BillingDetail(
            first_name=data['first_name'],
            last_name=data['last_name'],
            country=data['country'],
            address=data['address'],
            town=data['town'],
            postcode=data['postcode'],
            phone=data['phone'],
            email=data['email'],
            qr_code_image=qr_image,
             total=total
        )
        billing.save()
        return redirect('BillingList')
    
    return render(request, 'furniture/checkout.html', {
        'cart': cart,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    })


def billing_list(request):
    billings = BillingDetail.objects.all()
    return render(request, 'furniture/BillingList.html', {'billings': billings})


def shopping_cart(request):
    cart_data = get_cart_data(request)
    return render(request, 'furniture/cart.html', cart_data)


@require_POST
def update_cart_quantity(request):
    product_id = request.POST.get("product_id")
    quantity = int(request.POST.get("quantity"))

    cart = request.session.get("cart", {})

    if product_id in cart:
        cart[product_id]['qty'] = quantity

    request.session['cart'] = cart
    request.session.modified = True

    count = sum(item["qty"] for item in cart.values())
    total = sum(item["qty"] * float(item["price"]) for item in cart.values())

    items = []
    for pid, item in cart.items():
        items.append({
            "id": pid,
            "name": item["name"],
            "qty": item["qty"],
            "price": item["price"],
            "image": "",
        })

    return JsonResponse({
        "count": count,
        "total": total,
        "items": items
    })

def save_contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message"),
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')
    

# views.py (The 'checkout' view)
@login_required(login_url='login')
def checkout(request):
    # Get active QR codes (This is correct)
    qrs = QRCode.objects.filter(is_active=True) 

    # Get cart data
    cart_data = get_cart_data(request)
    subtotal = cart_data['total']
    shipping = 20  # Example shipping cost
    total = subtotal + shipping

    return render(request, "furniture/checkout.html", {
        "items": cart_data['items'],
        "subtotal": subtotal,
        "shipping": shipping,
        "total": total,
        "qrs": qrs, # This context variable is key
    })

# login_view, register_view, and logout_view would be defined here or imported if they are in another module.
def login_view(request):
    next_url = request.GET.get('next') or request.POST.get('next') or 'indexFur'
    
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']

        # Try to get user by email first
        try:
            user_obj = User.objects.get(email=username_or_email)
            username = user_obj.username
        except User.DoesNotExist:
            username = username_or_email

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)  # Redirect to next page if present
        else:
            messages.error(request, 'Invalid username/email or password.')

    return render(request, 'furniture/login.html', {'next': next_url})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('indexFur')

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        login(request, user)
        return redirect('indexFur')

    return render(request, "furniture/register.html")


def logout_view(request):
    logout(request)
    return redirect('indexFur')