
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import ClasseForm
from .models import Classe

import nltk

#nltk.download()

basetreinamento = [

('Dota ','game'),
('Battlefield ','game'),
('Don’t Starve','game'),
('Portal ','game'),
('Half-Life ','game'),
('Diablo III','game'),
('Overwatch','game'),
('pc game','game'),
('Destiny ','game'),
('Machinarium','game'),
('Mass Effect','game'),
('Metal Gear Solid V: The Phantom Pain','game'),
('jogar game','game'),
('Tom Clancy’s Rainbow Six: Siege','game'),
('Need for Speed: Most Wanted','game'),
('Brawlhalla','game'),
('Hearthstone','game'),
('Team Fortress','game'),
('Mortal Kombat ','game'),
('Rocket League','game'),
('Cities: Skylines','game'),
('Undertale','game'),
('Stardew Valley','game'),
('jogar para relaxar','game'),
('brincar para desestressar','game'),
('adoro jogar sozinho','game'),
('vencer a maquina','game'),
('passar de fase','game'),
('gosto de está no controle ','game'),
('trapacear','game'),
('ganha de meu amigo','game'),
('terrotar meus amigos','game'),
('ganhar todas','game'),
('não gosto de perder','game'),
('só jogo pra ganhar','game'),
('sou muito bom, passo de fase rápido','game'),
('perder todas','game'),
('gosto de corrida','game'),
('gosto de quebra-cabeça','game'),
('gosto de ação','game'),
('prefiro on-line','game'),
('brinco sempre','game'),
('treino todos os dias','game'),
('te desafio','game'),
('só uma partida','game'),
('só mas round','game'),
('The Legend of Zelda','game'),
('Ocarina of Time','game'),
('Super Mario World','game'),
('Grand Theft Auto V','game'),
('Age of Empires II','game'),
('League of Legends','game'),
('Breath of the Wild','game'),
('Dark Souls III','game'),
('The Witcher ','game'),
('Street Fighter','game'),
('World of Warcraft','game'),
('Quake','game'),
('pubg','game'),
('The Elder Scrolls V','game'),
('Skyrim','game'),
('The Last of Us','game'),
('Red Dead Redemption','game'),
('God of War','game'),
('Metal Gear Solid','game'),
('Snake Eater','game'),
('A Link to the Past','game'),
('Final Fantasy VII','game'),
('Horizon: Zero Dawn','game'),
('Grand Theft Auto: San Andreas','game'),

('desenhar','edition'),
('renderizar','edition'),
('colocar efeito','edition'),
('cortar','edition'),
('recortar','edition'),
('fundo musical','edition'),
('foco de luz','edition'),
('trabalhar com camadas','edition'),
('montar','edition'),
('extrair áudio','edition'),
('transição','edition'),
('dissolver','edition'),
('transformar','edition'),
('aparecer','edition'),
('desaparecer','edition'),
('surgir','edition'),
('filtro','edition'),
('contorno','edition'),
('cores','edition'),
('preenchimento','edition'),
('clipe de titulo','edition'),
('clipe de cor','edition'),
('trilha','edition'),
('monitor de video','edition'),
('trabalhar com imagens','edition'),
('editar imagens','edition'),
('editar vídeos','edition'),
('tratar videos','edition'),
('processamento de imagem','edition'),
('processamento de vídeos','edition'),
('efeito maquina de escrever','edition'),
('disfoque','edition'),
('efeito digitação','edition'),
('varios efeitos','edition'),
('iMovie','edition'),
('Movavi','edition'),
('Filmora','edition'),
('Openshot','edition'),
('Videopad','edition'),
('Camtasia','edition'),
('imagem svg','edition'),
('agrupar','edition'),
('desagrupar','edition'),
('preenchimento','edition'),
('contorno','edition'),
('exportar','edition'),
('caminho','edition'),
('curva','edition'),
('caneta','edition'),
('lapis','edition'),
('pincel','edition'),
('borracha','edition'),
('nos suave','edition'),
('editar nos','edition'),
('comprimir','edition'),
('expandir','edition'),
('boraco negro','edition'),
('girar','edition'),
('mascara','edition'),
('fluir em molde','edition'),
('transparencia','edition'),
('sobreposicao','edition'),
('morfologia','edition'),
('pele de tigre','edition'),
('padrao escoces','edition'),
('textura','edition'),
('mancha de tinta','edition'),
('aplicar sombra','edition'),
('borrifado a ouro','edition'),
('fresco fora','edition'),

('assistir filme','media'),
('videoconferência','media'),
('videoaula','media'),
('transmissão ao vivo','raiva'),
('transmissão em tempo real','media'),
('filme on-line','media'),
('aula on-line','media'),
('assistir live','media'),
('participar de reunião on-line','media'),
('fazer reunião on-line','media'),
('encontro on-line','media'),
('filme de terror','media'),
('documentário','media'),
('séries','media'),
('series policial','media'),
('fome de poder','media'),
('titanic','media'),
('eu robó','media'),
('alienigena','media'),
('velozes e furiosos','media'),
('até que a sorte nos separe','media'),
('a procura da felicidade','media'),
('cidade de deus','media'),
('tropa de elite','media'),
('um sonho de liberdade','media'),
('o poderoso chefão','media'),
('batman o cavaleiro das trevas','media'),
(' homens e uma sentênça','media'),
('o senhor dos anéis','media'),
('clube da luta','media'),
('matrix','media'),
('os setes samurais','media'),
('a vida é bela','media'),
('o silencio dos inocentes','media'),
('a felicidade não se compra','media'),
('guerra nas estrelas','media'),
('a espera de um milagre','media'),
('parasita','media'),
('interestelar','media'),
('o profissional','media'),
('os suspeitos','media'),
('harakiri','media'),
('stranger things','media'),
('emily em paris','media'),
('a maldição da Mansão Bly','media'),
('desejo Sombrio','media'),
('bom dia, Verônica','media'),
('anne with an e','media'),
('the umbrella academy','media'),
('good girls','media'),
('Heartland','media'),
('toy boy','media'),
('virgin river','media'),
('altered carbon','media'),
('ragnarok','media'),
('O ultimo guardião','media'),
('grace and frankie','media'),
('não fale com estranhos - the stranger','media'),
('vis a vis','media'),
('the witcher','media'),
('inacreditável','media'),
(' reasons why','media'),
('as telefonistas','media'),
('the ranch','media'),
('elite','media'),
('orange is the new black','media'),
('la casa de papel','media'),
('black mirror','media'),
('adoro filmes','media'),
('marvel - demolidor','media'),
('video aula','media'),

('trabalhos escolares','homeOffice'),
('pesquisas','homeOffice'),
('digitação de texto','homeOffice'),
('trablhar com planilhas','homeOffice'),
('fazer apresentações de slides','homeOffice'),
('edição de texto','homeOffice'),
('trabalho da escola','homeOffice'),
('instagran','homeOffice'),
('relatorios de vendas','homeOffice'),
('editar textos e planilhas','homeOffice'),
('planejamento','homeOffice'),
('trablhar com planilhas','homeOffice'),
('redação oficial','homeOffice'),
('folha de pagamento','homeOffice'),
('e-mail','homeOffice'),
('busca no google','homeOffice'),
('compra on-line','homeOffice'),
('pesquisa de preços','homeOffice'),
('tcc e artigos','homeOffice'),
('pacote office','homeOffice'),
('Word','homeOffice'),
('excel','homeOffice'),
('libreOffice','homeOffice'),
('writer','homeOffice'),
('calc','homeOffice'),
('trabalho simples','homeOffice'),
('trabalho acadêmico','homeOffice'),
('digitar texto','homeOffice'),
('leitura','homeOffice'),
('digitar um livro','homeOffice'),
('formatação de texto','homeOffice'),
('alinhamento de texto','homeOffice'),
('paginação','homeOffice'),
('secão','homeOffice'),
('dividi em colunas','homeOffice'),
('inserir formas','homeOffice'),
('tabelas','homeOffice'),
('curriculo','homeOffice'),
('cabeçalho e rodapé','homeOffice'),
('configurar pagina','homeOffice'),
('documentos','homeOffice'),
('digitação documentos diversos','homeOffice'),
('ortografia','homeOffice'),
('etiqueta','homeOffice'),
('caixa de selecao','homeOffice'),
('caixa de texto','homeOffice'),
('marcadores','homeOffice'),
('numeracao','homeOffice'),
('italico','homeOffice'),
('negrito','homeOffice'),
('tachado','homeOffice'),
('sublinhado','homeOffice'),
('titulo','homeOffice'),
('subtitulo','homeOffice'),
('nota de rodape','homeOffice'),
('mala direta','homeOffice'),
('cola especial','homeOffice'),
('celula','homeOffice'),
('menu','homeOffice'),
('guias','homeOffice'),
('barra de titulo','homeOffice'),
('graficos','homeOffice'),
('tabela dinamica','homeOffice'),
('verificacao ortografica','homeOffice'),
('clonar formatacao','homeOffice'),
('imprimir','homeOffice'),
('visualizar impressao','homeOffice'),
('barra de formula','homeOffice'),
('barra de status','homeOffice'),
('macro','homeOffice'),
('anotacoes','homeOffice'),
('localizar e substituir','homeOffice'),
('inserir caractere especial','homeOffice'),
('cor da fonte','homeOffice'),
('disposicao do texto','homeOffice'),
('sobrescrito','homeOffice'),

('desenvolvimeto web','development'),
('desenvolvimento de aplicativos','development'),
('linguagem de programação python','development'),
('liguagem de programaçao java','development'),
('linguagem de programação go','development'),
('linguagem de programação ruby','development'),
('linguagem de programação c','development'),
('linguagem de programação php','development'),
('linguagem de programaçao javascript','development'),
('liguagem de programação flutter','development'),
('linguagem de programação kotlin','development'),
('linguagem de programação typescript', 'development'),
('liguagem de programação  swift','development'),
('banco de dados','development'),
('interface','development'),
('análise de requisitos','development'),
('levatamento de requitos','development'),
('desenvolvimento agil','development'),
('metodologia de desenvolvimento','development'),
('projeto de software','development'),
('prototipação','development'),
('arquitetura cliente servidor','development'),
('arquitetura de desenvolvimento','development'),
('mysql workbench','development'),
('mangodb','development'),
('mariadb','development'),
('postgresql','development'),
('django','development'),
('nodejs','development'),
('laravel','development'),
('angular','development'),
('react-native','development'),
('model','development'),
('análise de dados','development'),
('inteligência artificial','development'),
('aprendizado de máquina','development'),
('paradgma','development'),
('compilação','development'),
('depuracao','development'),
('indentar o codigo', 'development'),
('nomear vareavel de maneira intuitiva','development'),
('testes','development'),
('loop','development'),
('chamar função','development'),
('estrutura condicional','development'),
('logica de promamaçao','development'),
('comentar o codigo','development'),
('tratamento de erro','development'),
('padroes de projetos','development'),
('linguagem de alto nivel','development'),
('back-end','development'),
('buguizando','development'),
('codar','development'),
('codigo elegante','development'),
('comitar','development'),
('diretorio','development'),
('debugar','development'),
('foo','development'),
('funfa','development'),
('full-stack','development'),
('Hardware','development'),
('poo','development'),
('mvc','development'),
('mvt','development'),
('aprendizado supervisionado','development'),
('aprendizado não-supervisionado','development'),
('aprendizagem profunda','development'),
('componentes','development'),
('dev','development'),
('vetores e matrizes','development'),
('arquivo e registro','development')]

baseteste =[

('jogo todos os dias','game'),
('viciado em jogos','game'),
('adoro d','game'),
('gosto de jogo leve','game'),
('pc parrudo para jogar','game'),
('pc potente para jogo','game'),
('Fortnite','game'),
('League of Legends','game'),
('Counter-Strike: Global Offensive','game'),
('Minecraft','game'),
('The Witcher ','game'),
(' Call of Duty: Warzone','game'),
('Grand Theft Auto V','game'),
('Dark Souls III','game'),
('Apex Legends','game'),
('Red Dead Redemption ','game'),
('Path of Exile','game'),
('Sekiro: Shadows Die Twice','game'),
('Cuphead','game'),
('Hollow Knight','game'),
('Resident Evil  Remake','game'),
('Doom','game'),
('The Sims ','game'),
('The Elder Scrolls V Skyrim','game'),
('Disco Elysium','game'),
('Call of Duty : Modern Warfare','game'),
('StarCraft II','game'),
('Fallout ','game'),
('Monster Hunter World','game'),
('Batman Arkham City','game'),

('Lightworks','edition'),
('Pinnacle Studio','edition'),
('Wondershare Video Editor','edition'),
('Adobe Premiere','edition'),
('Sony Vegas','edition'),
('Adobe After Effects','edition'),
('Blender','edition'),
('Lightworks','edition'),
('Shotcut','edition'),
('kdenlive','edition'),
('Gimp','edition'),
('Photoscape','edition'),
('Paint.NET','edition'),
('Polarr','edition'),
('Adobe Photoshop','edition'),
('Adobe Illustrator','edition'),
('metal afiado','edition'),
('metal escovado','edition'),
('pintura a tinta','edition'),
('rugoso e brilhante','edition'),
('queijo suiço','edition'),
('ruido cruzado','edition'),
('chamas','edition'),
('escorrer','edition'),
('partilhas elastica','edition'),
('mapa de saturaçao','edition'),
('tela de linho','edition'),
('pixelizar','edition'),
('mare negra','edition'),
('litografia','edition'),

('o rei leão','media'),
('de volta para o futuro','media'),
('o pianista','media'),
('o exterminador do futuro','media'),
('tempos modernos','media'),
('hamilton','media'),
('pisicose','media'),
('gladiador','media'),
('luzes da cidade','media'),
('os infiltrados','media'),
('os intocavéis','media'),
('o grande truque','media'),
('túmulo dos vagalumes','media'),
('era uma vez no oeste','media'),
('casablanca','media'),
('cinema paradiso','media'),
('janela indiscreta','media'),
('narcos','media'),
('the crown','media'),
('vikings','media'),
('house of cards','media'),
('sherlock','media'),
('breaking bad','media'),
('perdidos no espaço','media'),
('manhunt: unabomber','media'),
('retribution','media'),
('mindhunter','media'),
('grey´s anatomy','media'),
('how to get away with murder','media'),
(' dark','media'),

('formatação condicional','homeOffice'),
('correção ortográfica','homeOffice'),
('resenha','homeOffice'),
('resumo','homeOffice'),
('questionário','homeOffice'),
('simulado','homeOffice'),
('oficio','homeOffice'),
('memorando','homeOffice'),
('redação','homeOffice'),
('despacho','homeOffice'),
('preâmbulo','homeOffice'),
('sumário','homeOffice'),
('referẽncias','homeOffice'),
('contos','homeOffice'),
('romance','homeOffice'),
('versos e prosa','homeOffice'),
('subscrito','homeOffice'),
('inserir hiperlink','homeOffice'),
('inserir comentarios','homeOffice'),
('ancora','homeOffice'),
('mesclar celulas','homeOffice'),
('definir intervalo','homeOffice'),
('linhas e colunas','homeOffice'),
('excluir linhas e colunas','homeOffice'),
('desloc','homeOffice'),
('procv','homeOffice'),
('autosoma','homeOffice'),
('funcao agora','homeOffice'),
('povoar','homeOffice'),
('centralizar','homeOffice'),

('rede neorais','development'),
('visão computacional','development'),
('html e css','development'),
('processamento de liguagem natural','development'),
('pagina web','development'),
('plataforma','development'),
('api','development'),
('integração de sistema','development'),
('serviços web','development'),
('microserviços','development'),
('linguagem de marcação','development'),
('linguagem estruturada','development'),
('sistema de controle de versao','development'),
('sistema de modelagem de dados','development'),
('firebug','development'),
('terminator','development'),
('oh my zsh','development'),
('gitkraken','development'),
('gitlab','development'),
('slack','development'),
('meistertask','development'),
('cuckoo team','development'),
('dbdesigner','development'),
('mockflow','development'),
('linguagem xml','development'),
('arquivo json','development'),
('git e github','development'),
('framework','development'),
('bootstrap','development'),
('folha de estilo','development')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu',
			'do', 'e', 'estou', 'esta', 'esta', 'ir', 'meu', 'muito', 'mesmo',
			'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
stopwordsnltk.append(stopwords)
stopwordsnltk.append('tao')

#*********Remoção de stopwords******************
def removestopwords(texto):
    questoes = []
    for (palavras, area) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        questoes.append((semstop, area))
    return questoes

#View
@login_required
def rm_stopwords(request):
	questoes=removestopwords(basetreinamento)
	return render(request, 'projint/rm_stopwords.html', {'questoes':questoes})

#***********Axtração dos radicais das palavras*************
def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    questoesstemming = []
    for (palavras, area) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        questoesstemming.append((comstemming, area))
    return questoesstemming

questoescomstemmingtreinamento = aplicastemmer(basetreinamento)
questoescomstemmingteste = aplicastemmer(baseteste)

#View
@login_required
def aplic_stemmer(request):
	questoescomstemmingtreinamentos = aplicastemmer(basetreinamento)
	return render(request, 'projint/aplic_stemmer.html',
	{'questoescomstemmingtreinamentos':questoescomstemmingtreinamentos})

#**********************Buscar palavras*************************
def buscapalavras(questoes):
    todaspalavras = []
    for (palavras, area) in questoes:
        todaspalavras.extend(palavras)
    return todaspalavras

palavrastreinamento = buscapalavras(questoescomstemmingtreinamento)
palavrasteste = buscapalavras(questoescomstemmingteste)

#View
@login_required
def busc_palavras(request):
	palavrastreinamentos = buscapalavras(questoescomstemmingtreinamento)
	return render(request, 'projint/busc_palavras.html',
	{'palavrastreinamentos':palavrastreinamentos})

#**************Buscar frequecias das palavras******************
def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequenciatreinamento = buscafrequencia(palavrastreinamento)
frequenciateste = buscafrequencia(palavrasteste)

#View
@login_required
def busc_frequencia(request):
	frequenciatreinamentos = buscafrequencia(palavrastreinamento)
	return render(request, 'projint/busc_frequencia.html',
	{'frequenciatreinamentos':frequenciatreinamentos})

#**************Buscar palavras unicas***********************
def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

palavrasunicastreinamento = buscapalavrasunicas(frequenciatreinamento)
palavrasunicasteste = buscapalavrasunicas(frequenciateste)

# #View
@login_required
def busc_palavras_unicas(request):
	palavrasunicastreinamentos = buscapalavrasunicas(frequenciatreinamento)
	return render(request, 'projint/busc_palavras_unicas.html',
	{'palavrasunicastreinamentos':palavrasunicastreinamentos})

#*************Extrair palavras*********************
def extratorpalavras(document):
    doc = set(document)
    caracteristicas = {}
    for palavras in palavrasunicastreinamento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

#caracteristicasquestao = extratorpalavras([''])

basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, questoescomstemmingtreinamento)
basecompletateste = nltk.classify.apply_features(extratorpalavras, questoescomstemmingteste)

# ******construção tabela de probabilidade**************
classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)
nltk.classify.accuracy(classificador, basecompletateste)
@login_required
def accuracy(request):
	message =''
	message = "(accuracy : " + str(round(nltk.classify.accuracy(classificador, basecompletateste) * 100, 2)) + "%)"
	context = {'message':message}
	return render (request, 'projint/accuracy.html', context)
#********Visualização de erros**************************
erros = []

for (questao, classe) in basecompletateste:
    resultado = classificador.classify(questao)
    if resultado != classe:
        erros.append((classe, resultado, questao))

# ***********Metrica: Matriz de Confusão**************
@login_required
def matriz_confusao(request):
	messages =''
	from nltk.metrics import ConfusionMatrix
	esperado = []
	previsto = []
	for (questao, classe) in basecompletateste:
		resultado = classificador.classify(questao)
		previsto.append(resultado)
		esperado.append(classe)

		messages = ConfusionMatrix(previsto, esperado)
	print(messages)
	context = {'messages':messages}
	return render (request, 'projint/matriz_confusao.html', context)
#******** Outras forma de avaliação*********************
# 1. Cenario
# 2. Numero de classes
# 3. ZeroRules 

# *****interface de usuario: processa a*****************
#frase e retorna a classe c/ respect prob.**************
def index (request):
	messages =''
	if request.method == 'POST':
		teste_input = request.POST.get("area", "")
		teste_input_stemming = []
		stemmer = nltk.stem.RSLPStemmer()
		for (palavrastreinamento) in teste_input.split():
			comstem = [p for p in palavrastreinamento.split()]
			teste_input_stemming.append(str(stemmer.stem(comstem[0])))
		
		novo = extratorpalavras(teste_input_stemming)

		messages = classificador.classify(novo)
		#distr = classificador.prob_classify(novo)
		#for classe in distr.samples():
		#	messages = teste_input + " - " + " é provável que se interessa por: " + classificador.classify(extratorpalavras(teste_input_stemming)
		#) + ". (probabilidade : " + str("%s: %f" % (classificador.classify(novo), distr.prob(classe))) + "%)"
	else:
		messages ="erro"
	context = {'messages': messages}
	return render(request, 'projint/form.html', context)

def avaliacao (request):
	context_avaliacao = extratorpalavras(context)
	return render(request, 'projint/avaliacao.html', context_avaliacao)

#**************View do administrador********************

#***********************home****************************
def login (request):
	return render(request, 'registration/login.html', {})

def logout (request):
	return render(request, 'registration/login.html', {})

#*********************listar classe*********************
@login_required
def classe_list(request):
	classes = Classe.objects.all()
	return render(request, 'projint/classe_list.html', {'classes':classes})

#*******************detalhe da classe*******************
@login_required
def classe_detail(request, pk):
	classe = get_object_or_404(Classe, pk=pk)
	return render(request, 'projint/classe_detail.html', {'classe':classe})

def recomendacao_detail(request, pk):
	classe = get_object_or_404(Classe, pk=pk)
	return render(request, 'projint/recomendacao.html', {'classe':classe})

#*******************Add classe************************
@login_required
def classe_new(request):
	if request.method == "POST":
		form = ClasseForm(request.POST, request.FILES)
		if form.is_valid():
			classe = form.save(commit=False)
			classe.author = request.user
			classe.save()
			return redirect('classe_detail', pk=classe.pk)
	else:
		form = ClasseForm()
	return render(request, 'projint/classe_edit.html', {'form':form})

#********************editar classe********************
@login_required
def classe_edit(request, pk):
	classe = get_object_or_404(Classe, pk=pk)
	if request.method == "POST":
		form = ClasseForm(request.POST, request.FILES, instance=classe)
		if form.is_valid():
			classe = form.save(commit=False)
			classe.author = request.user
			classe.save()
			return redirect('classe_detail', pk=classe.pk)

	else:
		form=ClasseForm(instance=classe)
	return render(request, 'projint/classe_edit.html', {'form':form})

#*******************remover classe*******************
@login_required
def classe_remove(request, pk):
	classe = get_object_or_404(Classe, pk=pk)
	classe.delete()
	return redirect('classe_list')