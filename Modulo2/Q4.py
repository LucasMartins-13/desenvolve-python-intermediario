class EventoRecorrente(EventoABC):
    def __init__(self, titulo, descricao, data_hora_inicial, data_hora_final, intervalo_repeticao):
        super().__init__(titulo, descricao)
        self._datas: List[DataHora] = []
        
        atual = DataHora()
        atual.data_hora = data_hora_inicial

        final = DataHora()
        final.data_hora = data_hora_final

        while atual._data_hora <= final._data_hora:
            nova_data = DataHora()
            nova_data.data_hora = atual.data_hora
            self._datas.append(nova_data)
            atual.data_hora = atual.somaDias(intervalo_repeticao)

    def isConcluido(self, indice):
        return self._datas[indice].isPassado()

    def __str__(self):
        resultado = ''
        for i, data in enumerate(self._datas):
            resultado += (f"Evento: {self._titulo}, Data: {data.data_hora}, "
                          f"Descrição: {self._descricao}, Concluido: {self.isConcluido(i)}\n")
        return resultado.strip()

    def editar_data_hora(self, antiga_str, nova_str):
        for data in self._datas:
            if data.data_hora == antiga_str:
                data