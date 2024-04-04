def MesporExtenso():

  dia = str(input("Digite o dia: "))
  mes = str(input("Digite o mês: "))
  ano = str(input("Digite o ano: "))

  extrair_mes = mes[1:2]


  meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
     "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]



  if len(dia) == 2 and len(mes) == 2 and len(ano) == 4:
    match extrair_mes:
      case "1":
        jan = meses[0]
        print(f"{dia}/{jan}/{ano}")

      case "2":
        fev = meses[1]
        print(f"{dia}/{fev}/{ano}")

      case "3":
        mar = meses[2]
        print(f"{dia}/{mar}/{ano}")

      case "4":
        abr = meses[3]
        print(f"{dia}/{abr}/{ano}")

      case "5":
        mai = meses[4]
        print(f"{dia}/{mai}/{ano}")

      case "6":
        jun = meses[5]
        print(f"{dia}/{jun}/{ano}")

      case "7":
        jul = meses[6]
        print(f"{dia}/{jul}/{ano}")

      case "8":
        ago = meses[7]
        print(f"{dia}/{ago}/{ano}")

      case "9":
        set = meses[8]
        print(f"{dia}/{set}/{ano}")

      case "10":
        out = meses[9]
        print(f"{dia}/{out}/{ano}")

      case "11":
        nov = meses[10]
        print(f"{dia}/{nov}/{ano}")

      case "12":
        dez = meses[11]
        print(f"{dia}/{dez}/{ano}")

  else:
    print("Data inválida!")







MesporExtenso()