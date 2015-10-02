arquivos = open('numeros.txt','w')

for linha in range(1,1000):
    arquivos.write('%d\n'%linha)

arquivos.close()
