from django.db import models

# Create your models here.
class Tag(models.Model):

    name = models.CharField(max_length=50, verbose_name="Etiqueta")

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name

class Project(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="projects")
    desc = models.TextField(verbose_name="Descripción")
    tags = models.ManyToManyField(Tag, verbose_name="Etiquetas")
    github = models.CharField(max_length=255,null=True)
    link = models.CharField(max_length=255,null=True, blank=True)
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.name

