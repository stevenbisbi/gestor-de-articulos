from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group_Invest(models.Model):
    nombre= models.CharField(max_length=60)
    linea= models.CharField(max_length=60)
    CATEGORIA_CHOICES = [
        ('Categoría A', 'A'),
        ('Categoría B', 'B'),
        ('Categoría C', 'C'),
        ('Categoría D', 'D'),
        ('Categoría E', 'E'),
    ]
    categoria = models.CharField(max_length=12, choices=CATEGORIA_CHOICES)
    
    class Meta:
        verbose_name = 'Grupo de Investigación'
        verbose_name_plural = 'Grupos de Investigación'
        
    def __str__(self) -> str:
        return self.nombre
    
class Autor(models.Model):
    nombre=models.CharField(max_length=60)
    fecha_nac= models.DateField()
    nacionalidad=models.CharField(max_length=60)
    email= models.EmailField(max_length=254, unique=True)
    id_grupo = models.ForeignKey(Group_Invest, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self) -> str:
        return self.nombre

class Tipo_articulo(models.Model):
    DEFAULT = 'default_value'
    INFORME_TECNICO = 'informe_tecnico'
    ACTA_CONGRESO = 'acta_congreso'
    REVISTA_CIENTIFICA = 'revista_cientifica'
    
    TIPO_CHOICES = [
        (DEFAULT, 'Default Value'),
        (INFORME_TECNICO, 'Informe Técnico'),
        (ACTA_CONGRESO, 'Acta de Congreso'),
        (REVISTA_CIENTIFICA, 'Revista Científica'),
    ]

    tipo = models.CharField(
        max_length=100,
        choices=TIPO_CHOICES,
        default=DEFAULT,  # Establece un valor por defecto de las opciones
    )
        
    def __str__(self) -> str:
        return self.tipo

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    palabras_clave=models.CharField(max_length=100)
    copia= models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=100)
    id_autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_tipo=models.ForeignKey(Tipo_articulo, on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
    def __str__(self) -> str:
        return self.titulo
    
class Informe_tecnico(models.Model):
    numero = models.IntegerField()
    centro_pub=models.CharField(max_length=100)
    fecha = models.DateField()
    id_articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Informe Técnico'
        verbose_name_plural = 'Informes Técnicos'
    
class Acta_congreso(models.Model):
    edicion = models.IntegerField()
    ciudad = models.CharField(max_length=60)
    fecha = models.DateField()
    tipo=models.CharField(max_length=60)    
    frecuencia=models.CharField(max_length=60)    
    pais=models.CharField(max_length=60)
    ano_primer_ed=models.DateField()
    id_articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Acta de Congreso'
        verbose_name_plural = 'Actas de Congreso'
    def __str__(self):
        return f"Acta {self.edicion} - {self.ciudad}"
    
class Revista_cientifica(models.Model):
    nombre= models.CharField(max_length=60)
    editor = models.CharField(max_length=60)
    ano_inicio = models.DateField()
    periodicidad= models.CharField(max_length=60)
    tema =models.CharField(max_length=60)
    num_edicion=models.IntegerField()
    paginas = models.CharField(max_length=20)
    ano_pub=models.IntegerField()
    id_articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Revista Científica'
        verbose_name_plural = 'Revistas Científicas'
        
    def __str__(self):
        return f"Revista {self.nombre} - {self.num_edicion}"
    
    