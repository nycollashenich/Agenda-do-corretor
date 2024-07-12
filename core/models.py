from django.db import models
from stdimage import StdImageField
import uuid
from django.utils.text import slugify


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criado em', max_length=100, auto_now_add=True)
    modificado = models.DateField('Atualizado em', max_length=100, auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Imovel(models.Model):
    TIPO_IMOVEL_CHOICES = [
        ('Casa', 'Casa'),
        ('Apartamento', 'Apartamento'),
        ('Terreno', 'Terreno'),
    ]
    
    CONDICAO_IMOVEL_CHOICES = [
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
        ('Reformado', 'Reformado'),
        ('Antigo', 'Antigo'),
        ('Em reforma', 'Em reforma'),
    ]

    tipo = models.CharField('Tipo de Imóvel', max_length=20, choices=TIPO_IMOVEL_CHOICES)
    rua = models.CharField('Rua', max_length=100)
    numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    cep = models.CharField('CEP', max_length=8)
    num_quartos = models.PositiveIntegerField('Número de Quartos')
    num_banheiros = models.PositiveIntegerField('Número de Banheiros')
    num_garagem = models.PositiveIntegerField('Número de Vagas na Garagem')
    pets = models.BooleanField('Aceita Pets', default=False)
    condicoes = models.CharField('Condições', max_length=20, choices=CONDICAO_IMOVEL_CHOICES)
    descricao = models.TextField('Descrição', blank=True)
    imagem = StdImageField('Imagem', blank=True,upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, blank=True)
    agenda = models.CharField('Agenda', max_length=100)

    # slugy
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.rua)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self):
        return self.rua
