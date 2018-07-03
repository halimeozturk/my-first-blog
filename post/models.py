from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.

class Post(models.Model): #models kütüphanesinden Model classı oluşturdur.
    user = models.ForeignKey('auth.User', verbose_name = 'Yazar')
    title=models.CharField(max_length=120,verbose_name='başlık')
    content=models.TextField(verbose_name='İçerik')
    publishing_date=models.DateTimeField(verbose_name='Yayınlanma Tarihi',auto_now_add=True)
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True, editable=False , max_length=130)


    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('detail' , kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Post,self).save(*args,**kwargs)


class Meta:
    ordering = ['-publishing_date','id']
