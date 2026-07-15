
## Inserindo os dados

num1 = input("insira o primeiro número:  " ) 
num2 = input("insira o segundo número:  " ) 
operacao = input("insira a operação:  " ) 

match operacao: 
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2
    case "%":
        res = num1 % num2
    case "**":
        res = num1 ** num2
    case "+":
        res = num1 + num2
    case "+":
        res = num1 + num2
        
print(f"Resultado é igual a {res}")
