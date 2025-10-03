from django.shortcuts import get_object_or_404, render
from rezervation.models import *
from .models import  Category, Occasion, Night, MediaFile
from rezervation.models import Mosque
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.db.models import Min

def index(request):
    if request.META['HTTP_HOST']=="mjes.ir" or "kodomjaa.ir":
        masjed_index(request)
    elif request.META['HTTP_HOST']=="kodom-masjed.com":
        get_current_site(request)
        mosques = Mosque.objects.all()
        return render(request, 'slider-home.html', {"mosques": mosques})


def rez_page(request, slug):
    mosque = get_object_or_404(Mosque, slug=slug)
    return render(request, 'media-tabs.html', {"mosque": mosque})


# masajed view

# distinguish the site
def get_current_mosque(request, mosque_slug=None):
    """
    اگر مسجد از روی دامنه/ساب‌دامنه مشخص باشه → همون رو برمی‌گردونه
    اگر روی دامنه اصلی باشیم → از slug مسجد در URL پیدا می‌کنه
    """
    site = get_current_site(request)
    try:
        # اول تلاش کن مسجد رو از روی Site پیدا کنی
        print(request.META['HTTP_HOST'])  # مشابه بالا
        return Mosque.objects.get(site=site)
    except Mosque.DoesNotExist:
        # اگر روی دامنه اصلی بودیم، باید slug اجباری باشه
        if mosque_slug:
            return get_object_or_404(Mosque, slug=mosque_slug)
        raise Http404("Mosque not found")

# index page of masjed
def masjed_index(request):
    mosque=get_current_mosque(request,)
    categorys=Category.objects.filter(mosque=mosque)
    mediafile_selected = MediaFile.objects.filter(Selected=True)
    return render(request, 'masjed_template.html',{"categorys":categorys,"mediafile_selected":mediafile_selected})


# live page of masjed
def masjed_emama_sajad_live(request):
    return render(request, 'live.html')


# report page of masjed
def masjed_emama_sajad_report(request):
    return render(request, 'report.html')


# media pagese of masjed


# ۱. لیست دسته‌بندی‌های یک مسجد
# def category_list(request, mosque_slug=None):
#     mosque = get_current_mosque(request, mosque_slug)
#     categories = mosque.categories.all()
#     return render(request, "archive_page_category.html",{"mosque": mosque, "categories": categories})


def year_list(request, category_slug, mosque_slug=None):
    mosque = get_current_mosque(request, mosque_slug)
    category = get_object_or_404(Category, slug=category_slug, mosque=mosque)
    occasions = (
        category.occasions
            .values('year')
            .annotate(first_id=Min('id'))
            .values_list('first_id', flat=True)
    )
    occasions = Occasion.objects.filter(id__in=occasions)
    return render(request, "archive_page_category.html", {"mosque": mosque, "category":category, "occasions":occasions})


def occasion_list(request, category_slug, year, mosque_slug=None):
    mosque = get_current_mosque(request, mosque_slug)
    category = get_object_or_404(Category, slug=category_slug, mosque=mosque)
    occasions = category.occasions.filter(year=year)
    return render(request, "archive_page_occasions.html", {
        "mosque": mosque, "category": category, "year": year, "occasions": occasions
    })


def night_list(request, category_slug,occasion_slug, mosque_slug=None):
    mosque = get_current_mosque(request, mosque_slug)
    category = get_object_or_404(Category, slug=category_slug, mosque=mosque)
    print(occasion_slug)
    occasion = get_object_or_404(Occasion, slug=occasion_slug, category__mosque=mosque)
    print("occation",occasion)
    nights = occasion.nights.all()
    print("empty",nights)
    return render(request, "archive_page_night.html", {"mosque": mosque, "occasion": occasion, "nights": nights,"category":category})


def media_list(request,category_slug,year,occasion_slug,night_slug, mosque_slug=None):
    mosque = get_current_mosque(request, mosque_slug)
    night = get_object_or_404(Night, slug=night_slug, occasion__category__mosque=mosque)
    media_files = night.media_files.all()
    return render(request, "archive_page_list_media.html", {"mosque": mosque, "night": night, "media_files": media_files})

def media_single(request,media_slug):
    media_files = MediaFile.objects.get(slug=media_slug)
    return render(request,'archive_singel_media.html',{"media_files":media_files})




