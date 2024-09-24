from django import forms
from .models import Group_Invest, Autor, Articulo, Acta_congreso, Informe_tecnico, Revista_cientifica

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group_Invest
        fields = ['nombre', 'linea', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'linea': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nac', 'nacionalidad', 'email', 'id_grupo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'id_grupo': forms.Select(attrs={'class': 'form-control'})  # Usando Select para la clave foránea
        }
        
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'palabras_clave', 'copia', 'ubicacion', 'id_autor', 'id_tipo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'palabras_clave': forms.TextInput(attrs={'class': 'form-control'}),
            'copia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_autor': forms.Select(attrs={'class': 'form-select'}),
            'id_tipo': forms.Select(attrs={'class': 'form-select'}),}
        labels = {
            'id_autor': 'Autor',
            'id_tipo': 'Tipo de Artículo',
        }

class ActaCongresoForm(forms.ModelForm):
    class Meta:
        model = Acta_congreso
        fields = ['edicion', 'ciudad', 'fecha', 'tipo', 'frecuencia', 'pais', 'ano_primer_ed', 'id_articulo']
        widgets = {
            'edicion': forms.NumberInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'frecuencia': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_primer_ed': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_articulo': forms.Select(attrs={'class': 'form-control'}),
        }
        
class InformeTecnicoForm(forms.ModelForm):
    class Meta:
        model = Informe_tecnico
        fields = ['numero', 'centro_pub', 'fecha', 'id_articulo']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'centro_pub': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_articulo': forms.Select(attrs={'class': 'form-control'}),
        }
        
class RevistaCientificaForm(forms.ModelForm):
    class Meta:
        model = Revista_cientifica
        fields = ['nombre', 'editor', 'ano_inicio', 'periodicidad', 'tema', 'num_edicion', 'paginas', 'ano_pub', 'id_articulo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'editor': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'periodicidad': forms.TextInput(attrs={'class': 'form-control'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
            'num_edicion': forms.NumberInput(attrs={'class': 'form-control'}),
            'paginas': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_pub': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_articulo': forms.Select(attrs={'class': 'form-control'}),
        }