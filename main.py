import shutil
import re
import os
import defines

def carregarHostOriginal():
    return open(defines.HOST_URL,"r")

def criarBackup():
    return shutil.copy2(defines.HOST_URL, defines.HOST_BACKUP)

def copiarHost():
    return shutil.copy2(defines.HOST_URL, defines.HOST_COPY)

def atualizarHostOriginal(host_origem):
    return shutil.copy2(host_origem, defines.HOST_URL)

def validarUrl(url):
    try:
        #TODO DEPOIS VALIDAR SE JÁ EXISTE ESSE HOST ADICIONADO 
        padrao_url = re.compile(defines.PADRAO_INPUT)

        with open(defines.HOST_COPY) as file:
            contents = file.read()
            if url in contents:
                raise Exception("Host ja adicionado")
        return padrao_url.search(url)
    except Exception as e:
        print('Caught this error: ' + repr(e))
        return False

def adicionarBloqueio(url):
    # if(temNavegadorAberto())
      #TODO AQUI IRÁ SER UM POPUP PERGUNTANDO, PARA FUNCIONAMENTO CORRETO DO BLOQUEADOR
      #É NECESSÁRIO FECHAR TODOS OS SEUS NAVEGADORES, DESEJA FECHAR?
        # if(!clienteFechouNavegador())
        #     break
    url_val = validarUrl(url)    
    if(url_val):
        url_val = url_val.group().lower() #get clean url.
        
        with open(defines.HOST_COPY, 'a') as file:
            file.write("\n" + defines.LOCAL_IP + 
                       " " * defines.BLANK_SPACE_IP + 
                       url_val + " " * defines.BLANK_SPACE_DESC)
            #em testes anteriores foi precisso adicionar http e https no inicio da url, porém rodando apenas com www... está bloqueando
            # file.write("\n" + LOCAL_IP + " "*BLANK_SPACE_IP + PADRAO_URL1 + url_val)            #http
            # file.write("\n" + LOCAL_IP + " "*BLANK_SPACE_IP + PADRAO_URL2 + url_val)            #https

# copiarHost()
# adicionarBloqueio("www.facebook.com")
# atualizarHostOriginal(defines.HOST_COPY)

# 127.0.0.1      www.FACEBOOK.COM            # FACEBOOK SITE
# 127.0.0.1 + BLANK_SPACE_IP + url + (preencher de vazio até a posicao 52) + descricao

# os.system("taskkill /im msedge.exe /f") # w10+
# os.system("taskkill /im edge.exe /f")
# os.system("taskkill /im firefox.exe /f")
# os.system("taskkill /im chrome.exe /f")

#verificar se algum navegador esta aberto
#se tiver pedir pra fechar ou opcao de fechar a força

#ser capaz de ler o arquivo host_copy e fazer uma lista com os hots para o local host (127..)
#isso é importante para listar na lista de hosts.

#IMPORTANTE!
#desenvolver a lista temporária, talvez adicionar hots , guardar num arquivo quais foram adicionados
#depois do tempo excluir 1 por 1 e atualizar o host original, em vez de salvar como backup.

# if(seExistHostBackup)
# {
#     pegar
# }
# else
# continua o programa, pq n é a primeira execucao.


def verificarBackup():
    if(not os.path.isfile(defines.HOST_BACKUP_ORIGINAL)):
        shutil.copy2(defines.HOST_URL, defines.HOST_BACKUP_ORIGINAL)
    else:
        print("ja tem")
if __name__ == "__main__":
    #construtor sempre que abrir o programa
    verificarBackup()