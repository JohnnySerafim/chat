#criar o hash zap 

 
# Título: HashZap
# Botão : Iniciar Chat
    # quando eu clicar no botão:
    # janela/ dialog / modal/ popup
         # Título : Bem vindo ao HashZap
         # Campo de texto : Escreva seu nome no chat
         # Botão: Entrar no chat
            # clicou no botão
            # fechar o Dialog
                # Criar o chat
                # Criar o campo de mensagem: Digite sua mensagem  
                # botão : Enviar
                    # quando clicar no botão:
                    # Envie a mensagem para o chat  

# Importa o flet 
import flet as ft 


# criar a função  principal (main) do seu aplicativo
def main (pagina: ft.Page):
   pagina.title = "EloNexu"
   

   #Criar os elementos 
   titulo = ft.Text("ELO | NEXU", text_align= "center", size=30, weight="bold",color="#d3d3d3")

# criando janela
   titulo_janela = ft.Text(
        """   👋 Bem-vindo ao Elo Nexu 
            Mais que conversa, conexão real.""",color="#d3d3d3d5")
   
   def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()



  # criar websocker -> tunel de comunicação
   pagina.pubsub.subscribe(enviar_mensagem_tunel)


   
   def enviar_mensagem(evento):
        mensagem = f"{campo_nome.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()

   campo_mensagem = ft.TextField(label="Escreva Sua Mensagem",on_submit=enviar_mensagem)
   botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
   chat = ft.Column()
   linha_mensagem = ft.Row([campo_mensagem,botao_enviar])
   def entrar_chat(evento):
        pagina.pubsub.send_all(f"{campo_nome.value} Entrou no Chat")
      # fechar ajanela / o Dialog
        janela.open= False
        #remover o titulo
        pagina.remove(titulo)
        # remover o o botão
        pagina.remove(botao_iniciar)
        
        # Criar o chat
        pagina.add(chat)
        # Criar o campo de mensagem: Digite sua mensagem
        # botão : Enviar
        #pagina.add(botao_enviar) 
        pagina.add(linha_mensagem) 
        
        pagina.update()
   campo_nome = ft.TextField(label="Digite seu nome", on_submit=entrar_chat)
   botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)


   janela = ft.AlertDialog( 
      title=titulo_janela, 
      content=campo_nome,
      actions=[botao_entrar]
      )
   

   def abrir_dialog(evento):
         print("Abriu")
         pagina.dialog= janela
         janela.open = True
         pagina.add(janela)
         pagina.update()

         
   botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

   # colocar os elementos na pagina
   pagina.add(titulo)
   pagina.add (botao_iniciar)
   





# rodar o seu aplicativo
ft.app(target=main, view=ft.WEB_BROWSER)

# Sempre que você clica e qualquer botão -> flet ele cria um evento 