from model.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.recebe_avaliacao("Gui", 10)
restaurante_praca.recebe_avaliacao("Lais", 8)
restaurante_praca.recebe_avaliacao("Emy", 5)
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_mexicano.alternar_estado()


def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()
