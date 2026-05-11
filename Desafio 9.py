class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        
    def exibir_dados(self):
        return f"Produto: {self.nome} - {self.quantidade} unidades"

class ProdutoPerecivel(Produto):
    # Sobrescrevendo o método da classe pai
    def exibir_dados(self):
        return f"[PERECÍVEL] {self.nome} - {self.quantidade} unidades (Atenção: Requer refrigeração!)"

class ProdutoDigital(Produto):
    # Sobrescrevendo o método da classe pai
    def exibir_dados(self):
        return f"[DIGITAL] {self.nome} - {self.quantidade} licença(s) (Pronto para download)"

produtos = [
    ProdutoPerecivel("Leite", 5),
    ProdutoDigital("Curso", 1)
]

for p in produtos:
    # O polimorfismo acontece aqui: o mesmo comando age de forma diferente dependendo do objeto
    print(p.exibir_dados())