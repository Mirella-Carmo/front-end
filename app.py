from flask import Flask, render_template
app = Flask(__name__)

from evento import Evento

palestra = Evento()
palestra.set_banner('https://s4.static.brasilescola.uol.com.br/be/2023/05/mao-humana-e-mao-robotica-tocando-um-grafico-digital-em-alusao-a-inteligencia-artificial.jpg')
palestra.set_titulo('Inteligência Artificial para o Mercado')
palestra.set_data_hora('29/04 às 19hrs')
palestra.set_local('Auditório UniVassouras')
palestra.set_descricao('Com seu estilo afiado e visão futurista, Tony Stark mergulha nos bastidores da inteligência artificial e revela como ela está redefinindo o mercado global. De algoritmos preditivos a sistemas autônomos, Stark mostra como a IA está acelerando processos, transformando empregos e moldando decisões em tempo real. Sempre provocador, ele levanta reflexões sobre ética, responsabilidade e inovação em ritmo acelerado. A palestra é uma combinação perfeita entre tecnologia de ponta, negócios e atitude visionária. Prepare-se para insights ousados, exemplos reais e, claro, um toque de sarcasmo genial. Para Stark, o futuro não é opcional — é inevitável. E está mais perto do que parece.')
palestra.set_nome_palestrante('Tony Stark')
palestra.set_foto_palestrante('https://t.ctcdn.com.br/jSEs-a2AsizaO2xZCQXcdbGPZW0=/i490793.jpeg')

workshop = Evento()
workshop.set_banner('https://www.levty.com/blog/assets/post/confira-quais-as-5-principais-tendencias-do-desenvolvimento-de-software-66a2870acae0ad57266773d9/tendencias-LEVTY.webp')
workshop.set_titulo('Desenvolvimento de Software')
workshop.set_data_hora('30/04 às 10hrs')
workshop.set_local('Centro de Convenções')
workshop.set_nome_palestrante('Felicity Smoak')
workshop.set_foto_palestrante('https://cinepop.com.br/wp-content/uploads/2019/05/190411-emily-bett-rickards-arrow-1.jpg')
workshop.set_descricao('Neste workshop, Felicity Smoak compartilha seu conhecimento afiado sobre desenvolvimento de software, segurança da informação e pensamento crítico. Com sua linguagem rápida, humor afiado e domínio técnico, ela guia os participantes por uma jornada que vai além do código. Desde as boas práticas de programação até segurança de sistemas, Felicity mostra como um(a) desenvolvedor(a) pode ser a força invisível por trás de grandes soluções. Prepare-se para dicas práticas, demonstrações ao vivo e reflexões sobre ética na tecnologia. Ela não ensina só a programar — ela ensina a pensar como uma verdadeira mente estratégica da TI. Com ela, você vai aprender: -Como escrever código limpo, seguro e eficiente - A importância da cibersegurança desde o início do projeto -Ferramentas que todo(a) dev moderno(a) precisa dominar -Como as soft skills são o diferencial num time de alto desempenho')

miniCurso = Evento()
miniCurso.set_banner("https://docplace-riomarca.s3.amazonaws.com/2023/08/5-apps-medico-deve-conhecer.jpg")
miniCurso.set_titulo("Criação de Aplicativos")
miniCurso.set_data_hora('02/05 às 18hrs')
miniCurso.set_local('Laboratório de Informática')
miniCurso.set_descricao('Em uma jornada além do código, Thomas A. Anderson (Neo), o mestre da Matrix, leva você a desvendar os mistérios do desenvolvimento de aplicativos de uma maneira única. Através deste minicurso, Neo ensina como “ver” o código por trás da interface, abordando temas como estrutura de dados, lógica de programação e boas práticas para criar soluções eficientes. Em um ambiente de aprendizado intenso, Neo compartilha suas técnicas para projetar sistemas robustos, com foco em performance e escalabilidade. Prepare-se para desafiar a realidade do desenvolvimento e transformar suas ideias em aplicativos que funcionam, com visão e precisão. O futuro está sendo codificado — e você é parte dele')
miniCurso.set_nome_palestrante('Thomas A. Anderson (Neo)')
miniCurso.set_foto_palestrante('https://www.oficialhostgeek.com.br/wp-content/uploads/2020/11/4ecffd396a18ab717e2d27de6b2396c21.jpg')

from palestrante import Palestrante

palestra1 = Palestrante()
id = palestra1.set_id(1)
palestra1.set_foto('https://s2-valor.glbimg.com/6r7EXCo-eLrg6nWbSkGLTYB9KBo=/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_63b422c2caee4269b8b34177e8876b93/internal_photos/bs/2019/B/O/MSPOfAQfAtCmBYfTZpDg/tony-star-homem-de-ferro-1-div-paramount.jpg')
palestra1.set_nome('Tony Stark')
palestra1.set_data_hora('29/04 às 19hrs')
palestra1.set_descricao_carreira('Tony Stark é um gênio bilionário, inventor e CEO das Indústrias Stark. Formado pelo MIT aos 17 anos, destacou-se desde cedo pela sua mente brilhante na engenharia elétrica, mecânica e, mais recentemente, em Inteligência Artificial. Após um momento decisivo em sua vida, Tony redirecionou suas habilidades tecnológicas para criar soluções voltadas à proteção global.')
palestra1.set_nome_evento('Inteligência Artificial para o Mercado')

workshop1 = Palestrante()
id = workshop1.set_id(2)
workshop1.set_foto('https://static1.purebreak.com.br/articles/6/17/56/6/@/87621-uma-dose-da-felicity-emily-bett-580x0-3.jpg')
workshop1.set_nome('Felicity Smoak')
workshop1.set_data_hora('30/04 às 10hrs')
workshop1.set_descricao_carreira("Felicity Smoak é uma especialista em TI e desenvolvedora de software altamente habilidosa. Formada pelo MIT, construiu sua carreira unindo inteligência, ética e tecnologia de ponta. Com vasta experiência em segurança digital, sistemas complexos e desenvolvimento de aplicações, atuou como peça-chave em operações estratégicas. Ao longo dos anos, Felicity se tornou referência na criação de soluções inteligentes, com foco em impacto social e eficiência.")
workshop1.set_nome_evento('Desenvolvimento de Software')

miniCurso1 = Palestrante()
id = miniCurso1.set_id(3)
miniCurso1.set_foto('https://www.zbrushcentral.com/uploads/default/original/4X/b/9/5/b9503fcb3a573a56846b5357bb792c5308c998a5.jpeg')
miniCurso1.set_nome('Thomas A. Anderson (Neo)')
miniCurso1.set_data_hora("02/05 às 18hrs")
miniCurso1.set_descricao_carreira("Neo, ou Thomas Anderson, iniciou sua carreira como programador e analista de sistemas, ganhando destaque por suas habilidades em engenharia de software e desenvolvimento full stack. Com uma mente analítica e curiosa, ele dominou linguagens de programação e frameworks modernos, tornando-se referência em soluções digitais intuitivas e eficientes. Sua experiência prática em ambientes complexos o capacita a compartilhar uma visão única sobre o desenvolvimento de aplicativos voltados para impacto e inovação.")
miniCurso1.set_nome_evento('Criação de Aplicativos')

lista_palestrante = [palestra1, workshop1, miniCurso1]

from categorias import Categorias

categoria1 = Categorias()
categoria1.set_nome('Inteligência Artificial')
categoria1.set_imagem('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuWgwZR3ztuuwy0wTlEsTa6A0roq4HvBMPUA&s')

categoria2 = Categorias()
categoria2.set_nome('Desenvolvimento de Software')
categoria2.set_imagem('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ72fj_4qCPYIbLU4gr1xXLE0Z__8-p2dyERg&s')

categoria3 = Categorias()
categoria3.set_nome('Desenvolvimento de Aplicativos')
categoria3.set_imagem('https://www.coopersystem.com.br/wp-content/uploads/2019/04/o-que-%C3%A9-um-software-sob-medida.png')

from listaPalestrante import Palestrante
palestrante1 = Palestrante()
palestrante1.set_nome('Tony Stark')
palestrante1.set_nome_evento('Inteligência Artificial para o Mercado')
palestrante1.set_imagem('https://s2-valor.glbimg.com/6r7EXCo-eLrg6nWbSkGLTYB9KBo=/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_63b422c2caee4269b8b34177e8876b93/internal_photos/bs/2019/B/O/MSPOfAQfAtCmBYfTZpDg/tony-star-homem-de-ferro-1-div-paramount.jpg')

palestrante2 = Palestrante()
palestrante2.set_nome('Felicity Smoak')
palestrante2.set_nome_evento('Desenvolvimento de Software')
palestrante2.set_imagem('https://static1.purebreak.com.br/articles/6/17/56/6/@/87621-uma-dose-da-felicity-emily-bett-580x0-3.jpg')

palestrante3 = Palestrante()
palestrante3.set_nome('Thomas A. Anderson (Neo)')
palestrante3.set_nome_evento('Criação de Aplicativos')
palestrante3.set_imagem('https://www.oficialhostgeek.com.br/wp-content/uploads/2020/11/4ecffd396a18ab717e2d27de6b2396c21.jpg')

@app.route('/')
def home():
    return render_template('home.html')

#* detalhes de cada evento
"""
COMO FAZER ROTAS
@app.route('/pessoa/<nome>')
def teste(nome):
    return 'Ola, ' + nome"""

@app.route('/detalhes/<int:id>')
def detalhes_evento(id):
    return render_template('detalhes.html')

@app.route('/detalhes')
def detalhes_palestra():
    return render_template('detalhes.html', detalhes = palestra)

@app.route('/detalhesWorkShop')
def detalhes_workshop():
    return render_template('detalhes.html', detalhes = workshop, rota_palestrante = 'palestrante_workshop')

@app.route('/detalhesMiniCurso')
def detalhes_miniCurso():
    return render_template('detalhes.html', detalhes = miniCurso, rota_palestrante = 'palestrante_minicurso')

#* palestrantes de cada evento

@app.route('/palestrante/<int:id>')
def palestrante_eventos(id):
    for palestrante in lista_palestrante:
        if palestrante.get_id() == id:
            return render_template('palestrante.html', palestrante = palestrante)
    return ('Ops, palestrante não encontrado')
"""
@app.route('/palestrante')
def palestrante_palestra():
    return render_template('palestrante.html', palestrante=palestra1)

@app.route('/palestrante/workshop')
def palestrante_workshop():
    return render_template('palestrante.html', palestrante=workshop1)

@app.route('/palestrante/minicurso')
def palestrante_minicurso():
    return render_template('palestrante.html', palestrante=miniCurso1)
"""

#* Categorias do evento
@app.route('/categorias')
def categoria_ia():
    return render_template('categorias.html', palestra = categoria1, workshop = categoria2, miniCurso = categoria3)

#* Lista com todos os palestrantes do evento
@app.route('/todos/palestrantes')
def todos_palestrantes():
    return render_template('lista_palestrantes.html', listaPalestrante = [palestrante1, palestrante2, palestrante3])