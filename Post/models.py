from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.text import slugify


class Post (models.Model):
    # Models kütüphanesinden model class ı çağırıldı(Kalıtım sağlandı)

    # Postta olacak veriler.

    user = models.ForeignKey('auth.User', verbose_name= 'Yazar')
    title = models.CharField (max_length=120, verbose_name='Başlık')  # başlık ve karakter sınırı.
    content = RichTextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField (verbose_name='Eklenme Tarihi', auto_now_add=True)
    image = models.FileField(null=True, blank= True) #null ve blank isteğe bağlı olduğunu gösterir
    slug = models.SlugField(unique=True, editable=False, max_length= 130)

    def __str__(self):
        return self.title  # Postun başlığı neyse onu gösterir.

    def get_absolute_url(self):  # hangi post nesnesinde çağrılırsa onun adresini hesaplayacak

        return reverse('post:detail', kwargs={'slug': self.slug})

        # return "/post/{}".format(self.id)

    # veriler models kütüphanesinden alındı.

    def get_create_url(self):

        return reverse('post:create')

    def get_update_url(self):

        return reverse('post:update', kwargs={'slug': self.slug})

    def get_delete_url(self):

        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug( self ):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1

        while Post.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug


    def save( self, *args, **kwargs ):

        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args,**kwargs)

    class Meta:
        ordering = ['-publishing_date']

class Comment(models.Model):
    post = models.ForeignKey('Post.Post', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name= 'İsim')
    content = models.TextField(verbose_name='Yorum')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Ekleme Tarihi')
    class Meta:
        ordering = ['-created_date']