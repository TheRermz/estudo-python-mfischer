from model.restaurante import Restaurante
from model.cardapio.item_cardapio import ItemCardapio
from model.cardapio.bebida import Bebida
from model.cardapio.prato import Prato

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.recebe_avaliacao("Gui", 10)
restaurante_praca.recebe_avaliacao("Lais", 8)
restaurante_praca.recebe_avaliacao("Emy", 5)
restaurante_praca.recebe_avaliacao("Emy", 50) # não entra nas notas cadastradas
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")
restaurante_mexicano.alternar_estado()

bebida_suco = Bebida("Suco de melancia", 5.0, "grande")
prato_paozinho = Prato("Pãozinho", 2.00, "O melhor pão da cidade")


def main():
    Restaurante.listar_restaurante()
    print(bebida_suco, prato_paozinho)

if __name__ == '__main__':
    main()
