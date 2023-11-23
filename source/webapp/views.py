from django.shortcuts import render
from webapp.cat_db import CatDB


def index_page(request):
    return render(request, template_name='index.html')


def actions_with_cat(request):
    cat = CatDB()
    cat_list = cat.cat_list
    if request.method == 'POST':
        if request.POST.get('name_cat'):
            name = request.POST.get('name_cat')
            cat.get_name(name)
            context = {'cat_list': cat_list}
            return render(request, 'cat_stats.html', context)
        elif request.POST.get('select'):
            action = request.POST.get('select')
            if action == "play":
                cat.play_cat()
                context = {'cat_list': cat_list}
                return render(request, 'cat_stats.html', context)
            elif action == "sleep":
                cat.sleep_cat()
                context = {'cat_list': cat_list}
                return render(request, 'cat_stats.html', context)
            elif action == "feed":
                cat.feed_cat()
                context = {'cat_list': cat_list}
                return render(request, 'cat_stats.html', context)
            else:
                context = {'cat_list': cat_list}
                return render(request, 'cat_stats.html', context)
        else:
            return render(request, template_name='index.html')


