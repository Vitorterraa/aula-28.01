from flask import Flask, render_template
import random

app = Flask(__name__)
         
         
#lista de cores para alterar o fundo do site

lista_cores = ["red",
               "blue",
               "green",
               "yellow",
               "pink",
               "purple"]

   
lista_curiosidades = [
    "Quase jogou no Real Madrid quando era criança",
    "Primeiro jogador a marcar gols em competições diferentes no mesmo ano",
    "Tem uma grande paixão por pôquer",
    "Seu nome foi inspirado no pai",
    "Fez um gol mais rápido que muitos jogadores da história"
]

lista_fotos = [
    "neymar1.webp",
    "neymar2.jpg",
    "neymar3.jfif",
    "neymar4.jfif",
    "neymar5.jpg"
]    

                                                        
#Aqui ir para todas as minhas rotas

@app.route("/")

def principal():
    cor_de_fundo = random.choice(lista_cores)
    curiosidade = random.choice(lista_curiosidades)
    foto = random.choice(lista_fotos)
    return render_template("principal.html", cor_de_fundo_html = cor_de_fundo, curiosidade_html = curiosidade, foto_html = foto)
    
    
@app.route("/sobre")


def pagina_sobre():
    cor_de_fundo = random.choice(lista_cores)
    return render_template("sobre.html", cor_de_fundo_html = cor_de_fundo)
    

app.run(debug=True)                                                                                 
                                                                                  
                                                                                                                                                      
                                                                                  
                                                                                  
                                                                                  
                                                                                  