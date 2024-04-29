from model.restaurante import Restaurante
from model.cardapio.item_cardapio import ItemCardapio
from model.cardapio.bebida import Bebida
from model.cardapio.prato import Prato
from model.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.recebe_avaliacao("Gui", 10)
restaurante_praca.recebe_avaliacao("Lais", 8)
restaurante_praca.recebe_avaliacao("Emy", 5)
restaurante_praca.recebe_avaliacao("Emy", 50) # não entra nas notas cadastradas
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")
restaurante_mexicano.alternar_estado()

bebida_suco = Bebida("Suco de melancia", 5.0, "grande")
bebida_suco.aplicar_desconto()
prato_paozinho = Prato("Pãozinho", 2.00, "O melhor pão da cidade")
prato_paozinho.aplicar_desconto()
prato_sobremesa = Sobremesa("Cheesecake", 10.0, "Doce", "Pequeno")
prato_sobremesa.aplicar_desconto()
restaurante_praca.add_ao_cardapio(bebida_suco)
restaurante_praca.add_ao_cardapio(prato_paozinho)
restaurante_praca.add_ao_cardapio(prato_sobremesa)


def main():
    Restaurante.listar_restaurante()
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
