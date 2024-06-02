from .models import *
from .forms import TagForm, AuthorForm, QuoteForm
import json
import psycopg2
from pathlib import Path

author_file= r'C:\programming.study\software\software-10\quotesite\quotes\authors.json'
quote_file = r'C:\programming.study\software\software-10\quotesite\quotes\quotes.json'
  
# try:
#     # пытаемся подключиться к базе данных
#     conn = psycopg2.connect(dbname='postgres', user='postgres', password='11111111', host='127.0.0.1')
# except:
#     # в случае сбоя подключения будет выведено сообщение в STDOUT
#     print('Can`t establish connection to database')



def add_author(el):
    print(el['fullname'])
    author= Author(fullname = el['fullname'],
    born_date=el['born_date'],
    born_location=el['born_location'],
    description=el['description'])
    return author

def add_quote(item, author_object ):
    tags = []
    for tag in item['tags']:
        try:
            obj = Tag.objects.get(tag=tag)
            if obj:
                tags.append(obj.id)
        except Tag.DoesNotExist:
            new_obj = Tag(tag=tag)
            new_obj.save()   
            tags.append(new_obj.id)    
    # tags = [Tag(tag=tag) for tag in item['tags']]
    # quote_ob = Quote(tags=tags,
    #     author= author_object,
    #     quote=item['quote'])
    quote_ob = Quote.objects.create(quote=item['quote'], author = author_object)
    quote_ob.save()
    # quote_ob.author = author_object
    quote_ob.tags.set(tags)
    
    return quote_ob



def creating_authors():
    with open(author_file, 'r+') as f:
            json_author = json.load(f)
    for el in json_author:
            author = add_author(el)
            author.save()

def creating_quotes():
    with open(quote_file, 'r+') as f:
            json_quote = json.load(f)
    for item in json_quote:
            aut_name = item['author']
            try:
                find_autor = Author.objects.get(fullname=aut_name)
                if find_autor:
                    
                        new_quote = add_quote(item, find_autor)
                        new_quote.save()
            except Exception:
                print('ERROR: Can\'t find this author\'s name')
                print(f"---------\n{aut_name}\n-----------")


def printing_all():
        notes = Author.objects()
        print("-------------------")
        for note in notes:
            print(note.to_mongo().to_dict())

        otes = Quote.objects()
        print("-------------------")
        for note in otes:
            print(note.to_mongo().to_dict())

def delete():
        quot = Quote.objects()
        for q in quot:
            q.delete()


if __name__=="__main__":
    creating_authors()
    creating_quotes()