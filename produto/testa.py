class Produto:
    # função construtora da classe
    def __init__(self, codigo, descricao, tipo, preco_unitario, qtde_estoque):
        # atributos da classe
        self.codigo = codigo
        self.descricao = descricao
        self.tipo = tipo
        self.preco_unitario = preco_unitario
        self.qtde_estoque = qtde_estoque
        self.arrayList = {} # Em python inicializa essa váriavel como dicionário
    
    def salvar_produto(self):
        self.arrayList = {'Código': self.codigo, 'Descricao': self.descricao, 'Tipo': self.tipo,
        'Preço unitário': self.preco_unitario, 'Qtde de estoque': self.qtde_estoque}

    def visualizar(self):
        for i, j in self.arrayList.items():
            print(f'{i} - {j}')
    
    def retirar_estoque(self, qtde):
        if self.qtde_estoque < qtde:
            return f'Erro! Quantidade em estoque é menor que a retirada'

        self.qtde_estoque -= qtde
        return self.qtde_estoque
    
    def entrar_estoque(self, qtde):
        self.qtde_estoque += qtde
        return self.qtde_estoque