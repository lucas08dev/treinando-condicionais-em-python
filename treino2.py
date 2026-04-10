nome = (input("Digite o seu nome: "))
serie = (input("Digite a sua sala: "))
nota = float(input("Digite sua nota (de 0 a 100): "))

if nota>=60:
    print("Parabéns", nome + ",", "você foi aprovado!")

else:
    print("Infelizmente você não atingiu a meta :/")
    print("Fale com a coordenação para agendar sua prova final.")
 
