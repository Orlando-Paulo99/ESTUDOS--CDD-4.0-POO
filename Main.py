from biblioteca import Escola, Professor,Quadra,Aluno

esc = Escola("Criando Devs", 81992624419, "Rua Subida Pedro braz")
print(f"{esc.nome} se encontra na {esc.endereco} e nosso numero para contato é {esc.telefone}")
esc.aulas()

prof1 = Professor("Orlando", 123
                 , "Padre inglês")
print(f"{prof1.nome} é o nosso cordenador dos professores,uma excelente profissional assim comos os demais professores ")
prof1.ensinar()

q1=Quadra("Pátio","terreo","Primeira a Direita")
q1.jogar()

a1=Aluno("Paulo","18 anos","Nova Descoberta")
print(f"{a1.nome} foi o nosso alunos destaque desse ano,onde ele conseguiu atingir a melhor nota do ENEM e conseguiu ingressar na faculdade dos EUA e irá curasar Ciência da Computação")
a1.nota()

a1.media(10,10)
