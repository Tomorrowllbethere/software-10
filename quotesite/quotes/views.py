from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator


from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag, Author, Quote
from .seed import creating_quotes, creating_authors

def delete_all():
    Author.objects.all().delete()
    Quote.objects.all().delete()
    Tag.objects.all().delete()

def filling_db():
    creating_authors()
    creating_quotes()


def main(request):

    authors = Author.objects.filter().all()
    # виведення найпопулярніших тегів
    popular_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:5]
    
    # пагінація головної сторінки
    quotes = Quote.objects.filter().all()
    paginator = Paginator(quotes, 5)  # 5 цитат на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quotes/index.html', {
        'page_obj': page_obj,
        'popular_tags': popular_tags
    })


@login_required
def author(request):
    if request.method == 'POST':
            form = AuthorForm(request.POST)
            new_auth = form.save(commit=False)
            if form.is_valid():
                new_auth.save()
                return redirect(to='quotes:main')
            else:
                return render(request, 'quotes/author.html', {'form': form})
    else:
        form = AuthorForm()  # Створюємо новий екземпляр форми при GET запиті
        return render(request, 'quotes/author.html', {'form': form})



@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        new_tag = form.save()
    return render(request, 'quotes/note.html', {'tags' : new_tag})

@login_required
def note(request):
    tags = Tag.objects.filter().all()
    authors = Author.objects.filter().all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        new_note = form.save(commit=False)
        if form.is_valid():
            choice_authors = Author.objects.filter(id=request.POST.get('authors'))
            # print([i for i in choice_authors])
            for author in choice_authors:
                new_note.author = author
            
            new_note.save()
            
            tags_list = request.POST.getlist('tags')
            choice_tags = Tag.objects.filter(id__in=[tag for tag in tags_list])    
            for tag in choice_tags:
                    new_note.tags.add(tag)
            new_note.save()
            new_tags = request.POST.get('new_tags', '')
            if new_tags:
                new_tag_list = [tag.strip() for tag in new_tags.split(',') if tag.strip()]
                for tag_name in new_tag_list:
                        tag, created = Tag.objects.get_or_create(tag=tag_name)
                        new_note.tags.add(tag)
            new_note.save()



            return redirect(to='quotes:main')
        
        else:
            return render(request, 'quotes/note.html', {
                'tags': tags, 
                'form': form, 
                'authors': authors
            })

    return render(request, 'quotes/note.html', {
        'tags': tags, 
        'form': QuoteForm(), 
        'authors': authors
    })


def detail(request, note_id):
    author = get_object_or_404(Author, id=note_id)
    return render(request, 'quotes/detail.html', {"author": author})

def extract_tags(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    quotes = Quote.objects.filter(tags=tag).all()
    return render(request, 'quotes/temp.html', {'tag': tag, 'quotes': quotes})



@login_required
def delete_note(request, note_id):
    Quote.objects.get(pk=note_id, user=request.user).delete()
    return redirect(to='qoutes:main')
