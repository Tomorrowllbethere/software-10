from django.db import models


from django.db.models import Func

class MD5(Func):
    function = 'MD5'


class Author(models.Model):

    fullname = models.CharField(max_length=50, null=False, unique=True)
    born_date= models.CharField(max_length=50, null=False)
    born_location= models.CharField(max_length=80, null=False)
    description= models.TextField()

    def __str__(self):
        return f"{self.fullname},\n{self.born_date},\n{self.born_location},\n{self.description}"
    
    class Meta:
        indexes = [
            models.Index(MD5('description'), name='author_description_idx')
        ]

class Tag(models.Model):
    tag = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.tag}"

class Quote(models.Model):
    
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    quote= models.TextField(max_length=1350, null=False)
    tags= models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.quote}"