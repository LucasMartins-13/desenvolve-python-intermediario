evento1 = EventoUnico('Prova de Matemática', 'Capítulo 2 e 3', '15/06/2025, 08:00')
evento2 = EventoUnico('Consulta Médica', 'Cardiologista', '20/06/2025, 10:30')
evento3 = EventoRecorrente('Aula de Inglês', 'Sala 204', '01/06/2025, 14:00', '01/09/2025, 14:00', 30)

lista_eventos = [evento1, evento2, evento3]

[print(e) for e in lista_eventos];
