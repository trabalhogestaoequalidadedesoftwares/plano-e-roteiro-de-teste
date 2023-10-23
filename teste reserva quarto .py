class Hotel:
    def _init_(self, total_quartos):
        self.total_quartos = total_quartos
        self.quartos_disponiveis = total_quartos

    def reservar_quarto(self, quantidade_quartos):
        assert quantidade_quartos > 0, "A quantidade de quartos a reservar deve ser maior que zero."
        assert quantidade_quartos <= self.quartos_disponiveis, "Não há quartos suficientes disponíveis."
        self.quartos_disponiveis -= quantidade_quartos
        print(f"Reserva efetuada para {quantidade_quartos} quartos. Quartos disponíveis: {self.quartos_disponiveis}")

    def verificar_disponibilidade(self):
        print(f"Quartos disponíveis: {self.quartos_disponiveis}")


# Testes com assert

hotel = Hotel(total_quartos=50)  # Instantiate an object of Hotel
hotel.reservar_quarto(3)  # Reserva 3 quartos
assert hotel.quartos_disponiveis == 47, "Erro: número incorreto de quartos após a reserva."

hotel.reservar_quarto(45)  # Tenta reservar 45 quartos (mais do que o disponível)
assert hotel.quartos_disponiveis == 47, "Erro: número incorreto de quartos após uma tentativa de reserva inválida."