question = input("Enter right here the year than you born:")

year = int(question)

answer = (2025 - year)

print(f"So, about your answer, do you have {answer} years old, right?") 

tem_18 = True
tem_cartao = False

if tem_18 and tem_cartao:
    print("Pode tomar cervejinha")

tem_pai = False
tem_mae = True

if tem_pai or tem_mae:
    print("Pode entrar no parque de diversões")

rolando_assalto = True

if not rolando_assalto:
    print("Pode sair para mais um dia tranquilo no rio de janeiro")