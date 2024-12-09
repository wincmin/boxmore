from django.db import models

class Produto(models.Model):
    # Campos do produto
    categoria = models.CharField(max_length=100, verbose_name="Categoria")
    nome_produto = models.CharField(max_length=200, verbose_name="Nome do Produto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    cor = models.CharField(max_length=50, blank=True, null=True, verbose_name="Cor")
    marca = models.CharField(max_length=100, blank=True, null=True, verbose_name="Marca")
    qntd = models.PositiveIntegerField(verbose_name="Quantidade em Estoque")
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name="Imagem do Produto")
    
    # Campos opcionais específicos para livros (caso aplicável)
    autor = models.CharField(max_length=200, blank=True, null=True, verbose_name="Autor")
    ano_lancamento = models.IntegerField(blank=True, null=True, verbose_name="Ano de Lançamento")
    genero = models.CharField(max_length=100, blank=True, null=True, verbose_name="Gênero")

    def __str__(self):
        return self.nome_produto

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome_produto']
