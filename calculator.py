def plus(num1, num2):
  return num1+num2
def minus(num1, num2):
  return num1-num2
def umnz(num1, num2):
  return num1*num2
def delen(num1, num2):
  return num1/num2

while True:
  num1=int(input("\nВведите первое число: "))
  num2=int(input("Введите второе число: "))
  print("Выберите операцию")
  print("[+] - Сложение")
  print("[-] - Вычитание")
  print("[*] - Умножение")
  print("[/] - Деление")
  print("[exit or ' '] - Выход")

  menu=input("Введите символ операции: ")

  if menu=="+":
    print(num1, "+", num2, "=",plus(num1, num2))
  elif menu=="-":
    print(num1, "-", num2, "=", minus(num1, num2))
  elif menu=="*":
    print(num1, "*", num2, "=", umnz(num1, num2))
  elif menu=="/":
    print(num1, "/", num2, "=", delen(num1, num2))  
  elif menu=="exit" or menu==" ":
    print("Выход из калькулятора")
    break
