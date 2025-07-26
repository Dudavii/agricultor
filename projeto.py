

c_morango ={'arr':5.0, 'mudas':100,'insumos':30, 'maobra':60, 'energia': 600}
b_morango =[8.000,500]

c_abacaxi ={'arr':6.0, 'mudas':150,'insumos':31, 'maobra':50, 'energia':700}
b_abacaxi =[3.000,510]


c_batata ={'arr':9.0, 'mudas':180,'insumos':50, 'maobra':70, 'energia':400}
b_batata =[4.000,600]


c_abobora ={'arr':5.0, 'mudas':60,'insumos':80, 'maobra':40, 'energia':300}
b_abobora =[5.000,200]


c_manga ={'arr':7.0, 'mudas':80,'insumos':100, 'maobra':75, 'energia':500}
b_manga =[2.000,200]

hect = int(input("Digite a quantidade de hectares: "))
prod = input("Digite o produtos: 1 morango , 2 abacaxi, 3 batata, 4 abobora , 5 manga:  ")

if prod == "1":
    soma = c_morango['arr'] + c_morango ['mudas'] + c_morango ['insumos'] + c_morango ['mao de obra'] + c_morango ['energia'] 
    valor = soma * hect
    print(valor)

    lucro_total = b_morango ['valor'] * b_morango ['kg/hec'] 
    print(lucro_total)
    lucro_liquido = lucro_total - valor 
    print(f"o lucro é : {lucro_liquido}" )

elif prod == "2":
    soma = c_abacaxi['arr'] + c_abacaxi ['mudas'] + c_abacaxi ['insumos'] + c_abacaxi ['mao de obra'] + c_abacaxi ['energia'] 
    valor = soma * hect
    print(valor)

    lucro_total = b_abacaxi ['valor'] * b_abacaxi ['kg/hec'] 
    print(lucro_total)
    lucro_liquido = lucro_total - valor 
    print(f"o lucro é : {lucro_liquido}" )


elif prod == "3":
    soma = c_batata['arr'] + c_batata ['mudas'] + c_batata ['insumos'] + c_batata['mao de obra'] + c_batata ['energia'] 
    valor = soma * hect
    print(valor)

    lucro_total = b_batata ['valor'] * b_batata ['kg/hec'] 
    print(lucro_total)
    lucro_liquido = lucro_total - valor 
    print(f"o lucro é : {lucro_liquido}" )

elif prod == "4":
    soma = c_abobora ['arr'] + c_abobora ['mudas'] + c_abobora ['insumos'] + c_abobora ['mao de obra'] + c_aborbora ['energia'] 
    valor = soma * hect
    print(valor)

    lucro_total = b_abobora ['valor'] * b_abobora ['kg/hec'] 
    print(lucro_total)
    lucro_liquido = lucro_total - valor 
    print(f"o lucro é : {lucro_liquido}" )


elif prod == "5":
  soma = c_manga ['arr'] + c_manga ['mudas'] + c_manga ['insumos'] + c_manga ['mao de obra'] + c_manga ['energia'] 
  valor = soma * hect
  print(valor)

  lucro_total = b_manga ['valor'] * b_manga ['kg/hec'] 
  print(lucro_total)
  lucro_liquido = lucro_total - valor 
  print(f"o lucro é : {lucro_liquido}" )

