import os
import time
import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv() 

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def program():
   funcs = ["chatbot", "impares e pares", "consoantes", "somar positivos e negativos ou -> sum", "max e min"]
   while True:
      cmd = input("Qual ferramenta quer usar? \n>>")
      if cmd == "/":
         print(funcs,"\n\n")
      elif cmd == "chatbot":
         print()
         chatbot()  
      elif cmd in ["impares e pares", "/impares", "/pares"]:
         print()
         impares_pares()
      elif cmd == "consoantes":
         print()
         consoantes()
      elif cmd in ["sum", "somar positivos e negativos"]:
         print()
         sum_positive()
      elif cmd == "max e min":
         print()
         max_and_min()
      elif cmd.lower() == "quit":
         break 
      else:
         print("Não existe essa opção.")
         print("Opções: \n\n")
         print(funcs)

def consoantes():
   cons = "bcdfghjklmnpqrstvxz"
   word_cons = []
   prhase = input("Escreva a sua palavra: \n>> ").lower()
   if prhase == "quit":
      return
   for word_prhase in prhase.split():
      for w in word_prhase:
         if w in cons:
            if w not in word_cons: 
               word_cons.append(w)
      if len(word_cons) == 0:
         print("Não tem consoantes nessa palavra.")
         print()
         return
   print("Quantidade de consoantes presentes na palavra", len(word_cons))
   print("Consoantes presentes na palavra: ", word_cons)
   print()

def max_and_min():
   nums = input("Digite os números com espaço entre eles: \n>> ")
   nums_part = nums.split()
   list_nums = []
   for n in nums_part:
      num_int = int(n)
      if num_int not in list_nums:
         list_nums.append(num_int)
   print("O maior número entre esses é o: ", max(list_nums))
   print("O menor número entre esses é o: ", min(list_nums))
   print()

def sum_positive():
   nums = input("Escreva os números separados por espaço: \n>> ").strip()
   nums_parts = nums.split(" ")
   positives = []
   negatives = []
   for n in nums_parts:
      num = float(n)
      if num  > 0:
         positives.append(num)
      else:
         negatives.append(num)
   print("A soma dos negativos é: ", sum(negatives))
   print("A soma dos positivos é: ", sum(positives))
   print()


def impares_pares():
   pares = []
   impares =[]
   num = int(input("Digite um número: \n>> "))
   for n in range(num + 1):
      if n % 2 == 0:
         pares.append(n)
      elif n.lower() == "quit":
         break
      else:
         impares.append(n)
   print("Números pares: ", pares)
   print("Números impares: ", impares)

def write(res, delay = 0.02):
    for letra in res:
        sys.stdout.write(letra)
        sys.stdout.flush()        
        time.sleep(delay)        
    print()
    print()  
      
def chatbot():
    print("Digite 'quit' para sair do chat. \n")
    msg = input("Fale comigo: \n>> ")
    print()
    
    while msg.lower() != "quit":
        chat_completion = client.chat.completions.create(
            messages=[
                  {"role": "system", "content": """Você é conversador e prestativo. responde até 500 caracteres.
                     caso o usuário pergunte como fechar o chat, diga pra ele que ele pode encerrar o bate papo escrevendo quit e apertando enter. """},
                  {"role": "user", "content": msg}
            ],
            model="llama-3.3-70b-versatile",
         )
        resposta = chat_completion.choices[0].message.content 
        write(resposta)
        msg = input("Voce: \n>> ")
        print()

if __name__ == "__main__":
   print(" --------- Digite barra ( / ) para opções: ---------")
   program()