from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from accounts.models import Product, CarouselSlide, AboutHeroImages, ProjectSectionHeader, Project,TeamSectionHeader,TeamMember, TeamMembers
from accounts.models import Product

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
    
    # Retrieve the Project Header Text
    project_header = ProjectSectionHeader.objects.first()
    
    # Retrieve all Projects
    projects = Project.objects.all()
    team_header = TeamSectionHeader.objects.first()
    team_members = TeamMember.objects.all()
    
    context = {
        'slides': slides,
        'about_images': about_images,
        'project_header': project_header, # New context variable
        'projects': projects,             # New context variable
        'team_header': team_header,       
        'team_members': team_members,
    }
    return render(request, 'furniture/index.html', context)

def aboutFur(request):
    return render(request, 'furniture/about.html')

def blogDetial(request):
    return render(request, 'furniture/blog_detail.html')

def blog(request):
    return render(request, 'furniture/blog.html')

def cart(request):
    return render(request, 'furniture/cart.html')

def checkOut(request):
    return render(request, 'furniture/checkout.html')

def contact(request):
    return render(request, 'furniture/contact.html')
def detail(request, pk): 
    project_item = get_object_or_404(Project, pk=pk) 
    context = {
        'project_item': project_item 
    }
    return render(request, 'furniture/detail.html', context)
def pricing(request):
    return render(request, 'furniture/pricing.html')

def shop(request):
    DTproducts = Product.objects.all()
    context = {
        'Objproducts': DTproducts

    }
    return render(request, 'furniture/shop.html', context)

def team(request):
    DTmembers = TeamMembers.objects.all()
    context = {
        "objDTmembers": DTmembers,
    }
    return render(request, 'furniture/team.html', context)


def team_detail(request, id):
    # Get the team member by ID
    member = get_object_or_404(TeamMembers, id=id)

    # Social links loop
    social_links = []
    if member.facebook:
        social_links.append({"url": member.facebook, "icon": "fa-facebook"})
    if member.telegram:
        social_links.append({"url": member.telegram, "icon": "fa-telegram"})
    if member.youtube:
        social_links.append({"url": member.youtube, "icon": "fa-youtube-play"})

    # Skills loop (using your model fields)
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
