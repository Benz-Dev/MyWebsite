from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50, verbose_name='Categoría')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=50, verbose_name="Título")
    image = models.ImageField(upload_to="blog", verbose_name="Imágen")
    content = RichTextField(verbose_name="Contenido")
    visible = models.BooleanField(verbose_name="¿Público?")
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    slug = models.SlugField(null=False, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        if visible == True:
            public = "Público"
        else:
            public = "Privado"
        return self.title + public
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})    
    

