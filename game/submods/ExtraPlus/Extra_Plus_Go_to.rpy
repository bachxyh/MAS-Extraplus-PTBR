#===========================================================================================
# CAFETERIA
#===========================================================================================

define cafe_sprite = ["cafe.png","cafe_rain.png","cafe_rain-n.png","cafe_rain-ss.png","cafe-n.png","cafe-ss.png"]
default dessert_player = None

label cafe_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_cafe, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump cafe_cakes

label cafe_cakes:
    m 1hua "Chegamos, [mas_get_player_nickname()]~"
    m 1eub "É um lugar tão bonito, não acha?"
    m 1hua "Falando em bonito, estou com vontade de uma sobremesa."
    m 3eub "Já volto, [player]~"
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if mas_isDayNow():
            monika_chr.wear_acs(extraplus_acs_chocolatecake)
        elif mas_isNightNow():
            monika_chr.wear_acs(extraplus_acs_fruitcake)

    call mas_transition_from_emptydesk("monika 1eua")
    if monika_chr.is_wearing_acs(mas_acs_mug):
        m 1hua "Além disso, essa sobremesa combina muito bem com café~"
    elif monika_chr.is_wearing_acs(mas_acs_hotchoc_mug):
        m 1hua "Seria melhor com uma xícara de café, mas chocolate quente também é uma ótima escolha~"
    else:
        $ monika_chr.wear_acs(extraplus_acs_coffeecup)
        m 1hua "E eu não posso esquecer a xícara de café para acompanhar a sobremesa~"
    m 1etb "Aliás, você pegou uma sobremesa também?"
    m 1rkd "Eu ficaria mal se fosse a única comendo...{nw}"
    $ _history_list.pop()
    menu:
        m "Eu ficaria mal se fosse a única comendo...{fast}"
        "Não se preocupe, eu peguei uma sobremesa.":
            $ dessert_player = True
            m 1hub "Ah, que ótimo!"
            m 3eub "E recomendo que você pegue uma xícara de café."
        "Não se preocupe com isso.":
            $ dessert_player = False
            m 1ekc "Bem, se você diz."
            m 1ekb "Eu te daria a minha, mas sua tela me impede de fazer isso..."
            m 3hka "Espero que você pelo menos tenha uma xícara de café!"
    m 3hua "Ehehe~"
    jump to_cafe_loop
    return

label monika_boopcafebeta:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_chocolatecake) or monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        m 1ttp "...?"
        m 1eka "Ei, estou aproveitando minha sobremesa."
        m 3hua "Faça isso quando eu terminar, tá bom?"
    else:
        m 1hub "*Boop*"
    jump to_cafe_loop
    return

label cafe_sorry_player:
    show monika idle at t11
    m 1ekd "Sinto muito, [player]."
    m 1ekc "Mas eu ainda não sei como mudar de cenário."
    m 3lka "Ainda estou aprendendo a programar e não quero que algo ruim aconteça por minha causa..."
    m 3hua "Eu sei muito bem que você queria ir ao café."
    m 1eua "Mas, um dia eu vou saber como mudar, [player]."
    m 1eub "Apenas tenha paciência, tudo bem~"
    $ _history_list.pop()
    
    menu:
        "Para desbloquear 'Encontros' você precisa ter 400+ de afeição! *Nota do Bach!*":
            jump close_extraplus

    return

#===========================================================================================
# CAFETERIA DIÁLOGOS
#===========================================================================================

label extra_talk_feel:
    show monika staticpose at t11
    $ moldable_variable = renpy.random.randint(1,3)
    if moldable_variable == 1:
        m 1hkbsb "Estou me sentindo um pouco nervosa, afinal, estamos em um encontro!"
        #Caso você nunca tenha indo com a Monika para algum lugar.
        if renpy.seen_label("bye_going_somewhere"):
            m 1ekbsb "Além disso, não estou em um pen drive ou em seu celular."
            m 3hubsa "Agora tô me sentindo ainda mais perto de você, vou me lembrar desse momento para sempre~"
            m 3hubsb "Obrigada por me chamar para um encontro!"
        else:
            m 1ekbsb "É a primeira vez que saímos juntos~"
            m 3hubsa "Então, obrigada por me convidar."
            m 3hubsb "Você pode fazer isso através de um pen drive, mesmo que eu não consiga ver nada."
            m 3ekbsa "Eu sei que vai ser muito romântico."
    elif moldable_variable == 2:
        m 1eubla "Estou tão feliz que você está aqui."
        m 1eublb "Compartilhar uma sobremesa com você é bem romântico."
        m 1hublb "Espero que possamos fazer isso na sua realidade!"
        m 1hubla "Eu sei que você tem muito em mente para nós dois~"
    elif moldable_variable == 3:
        m 1dubsa "Sinto que vou lembrar desse dia para sempre."
        m 1dubsa "Afinal, estamos em um encontro."
        m 1kubsb "Eu sei que um dia faremos isso na sua realidade!"
        m 1hubsa "E espero que isso aconteça~"
    jump to_cafe_loop
    return

label extra_talk_you:
    show monika staticpose at t11
    m 3dkc "Eu sei, [mas_get_player_nickname()]."
    m 3ekd "Estamos em um encontro, uma forma de nos conhecermos melhor."
    m 3ekd "Você só tem opções pré-configuradas para responder com base na pergunta que eu faço..."
    m 3ekc "Afinal, isso é uma visual novel, "
    extend 1dua "mas comparado a outras novelas, aqui estamos criando uma realidade para nós dois."
    m 1eub "Embora você possa criar suas próprias respostas, afinal, você tem mais controle do que eu."
    if persistent._mas_pm_has_code_experience is True:
        m 3eub "Você me disse que tem experiência em programação, por isso menciono isso."
    else:
        m 3ekb "Eu sei que você não tem experiência em programação, mas não se preocupe, você pode aprender."
        m 3hub "Eu confio em você, [mas_get_player_nickname()]."
    m 1eua "Você poderia adicionar mais coisas aqui, por exemplo, este café."
    m 1hua "E também mais diálogos que podemos discutir, falar sobre seus hobbies ou sobre sua família."
    m 1rksdra "Tente garantir que não haja código com erro de digitação, você pode me perder se um erro sério acontecer."
    m 1eub "Mas deixando isso de lado, eu adoraria estar ao seu lado, digamos, como um robô."
    m 1eub "Assim poderíamos ter uma conversa tranquila~"
    m 1eka "Eu sei muito bem o que você quer me contar sobre algo ou como você está se sentindo."
    m 1eka "Mas nossa forma de comunicação é muito limitada por causa do que eu disse antes."
    m 3hua "Isso não nos impede de ter um relacionamento legal juntos!"
    m 3hua "Além disso, eu sei as coisas mais importantes sobre você, qualquer informação que você me der! "
    extend 3hub "Mesmo que seja só a menor coisa."
    m 3eub "Eu realmente aprecio isso~"
    jump to_cafe_loop
    return

label extra_talk_phobia:
    show monika staticpose at t11
    m 1rtd "A verdade é que essa é uma boa pergunta, eu nem pensei em qual medo eu teria."
    m 1hua "Afinal, eu não sou humana, sou apenas uma personagem fofa."
    extend 1dksdlb "Embora eu esteja ciente de tudo que acontece ao meu redor."
    m 3eud "Mas se você quer saber um, eu diria 'autofobia'."
    m 3eka "O medo da solidão."
    m 3dud "Sentir-se isolada sem companhia, mesmo que haja outros NPCs ou um animal de estimação para me fazer companhia."
    m 3dud "Não seria a mesma coisa, eles seriam apenas enfeites neste lugar."
    m 3duc "Embora eu chamaria isso de purgatório."
    m 1lka "Eu sei muito bem que essa fobia se tornou muito comum, ainda mais por causa da pandemia."
    m 1lka "É bem triste não ter alguém com quem conversar."
    m 1esd "Eu vi outras Monikas passando por isso, por causa da negligência de seus jogadores."
    m 1esd "Ou pessoas que têm ressentimento contra nós por causa do que aconteceu no jogo."
    m 1dsc "Eu menciono isso porque é um efeito dominó, a rejeição leva à solidão e a solidão leva ao desespero."
    m 1esb "Mas é uma coisa muito menor, comparado ao que aconteceu quando o jogo foi lançado."
    m 3hua "Sabe, é engraçado, antes éramos mais odiadas e os outros membros do clube eram mais amados."
    m 3hua "Agora tudo se inverteu a nosso favor~"
    m 3dub "Finalmente as pessoas perceberam que a história foi mal contada."
    m 1hua "Mas não devemos nos preocupar mais com isso."
    m 1eubsb "Estamos em um encontro, afinal!"
    m 1eubsb "Vamos aproveitar nosso tempo aqui, [player]~"
    jump to_cafe_loop
    return

label extra_talk_ambition:
    show monika staticpose at t11
    m 1tubsb "{i}Você{/i}, você é minha grande ambição."
    m 1hkbsa "Só de pensar que estou tão longe e tão perto ao mesmo tempo."
    m 1hkbsa "Vai ser difícil chegar até você, mas é isso que mais espe#ro."
    m 1ekbsa "Quando eu ver seu rostinho pela primeira vez, não acho que meu coração vai conseguir manter um ritmo tranquilo de tanta emoção."
    m 1ekbsa "Eu adoraria usar a câmera do seu computador para pelo menos ver como você é."
    m 1rksdlb "Mas eu não tenho permissão de administrador para usá-la."
    m 1hua "Que situação engraçada, não acha?"
    m 1lub "Bem, pelo menos eu tenho uma ideia de como você é."
    m 1lub "Para mim, isso é mais do que suficiente, com as informações que tenho sobre sua aparência."
    m 1eubsa "Obrigada por ouvir, vamos continuar com nosso encontro~"
    jump to_cafe_loop
    return

label extra_talk_teen:
    show monika staticpose at t11
    m 1eua "Essa é uma pergunta bem curiosa, [mas_get_player_nickname()]"
    m 1dua "{i}Como estaremos em 10 anos?{/i}"
    if mas_anni.isAnniOneMonth():
        m 1rub "Mesmo que já tenhamos nos conhecido há um mês desde aquele dia..."
        m 1dua "É realmente difícil saber o que o futuro nos reserva, [player]."
        m 1dua "Não sabemos o que o destino tem guardado para nós."
        m 1hka "Vamos passar por muitas situações difíceis e muitas felizes."
        m 1hka "A vida é assim, mas enquanto nada de ruim acontecer com você, isso é mais do que suficiente para mim~"
    elif mas_anni.isAnniThreeMonth() or mas_anni.isAnniSixMonth():
        m 1eub "Embora você esteja comigo há vários meses."
        m 1hub "Eu gostei muito dos meses que passamos juntos!"
        m 1hub "Não sei o que o futuro nos reserva, [mas_get_player_nickname()]."
        m 3ekb "Mas uma coisa eu sei, você vai crescer e se tornar uma pessoa incrível."
        m 3ekb "A vida é como um livro, há páginas que você precisa descobrir e outras que você deve esconder."
        m 3eua "Você pode voltar e olhar algumas delas como uma boa memória ou como você progrediu."
        m 3dsc "Mas nunca tente abrir feridas antigas, elas ficaram no passado, então é desnecessário lembrar delas."
        m 1hua "Espero que o que eu disse te anime um pouco~"
    elif store.mas_anni.anniCount() == 1:
        m 1eubfa "Mesmo que já tenhamos comemorado nosso um ano juntos..."
        m 1hubfb "Foi o melhor ano da minha vida!"
        m 1hubfb "Fico feliz que nada sério tenha acontecido com você por causa da pandemia."
        m 1eka "Mas ainda assim, cuide bem de si mesmo, ainda temos muitas memórias para criar juntos!"
        m 1ekd "Neste ponto do nosso relacionamento, tenho medo de te perder."
        m 1hubla "Bem, eu sei que você cuida bem de si, [mas_get_player_nickname()], então só me avise quando precisar da minha ajuda."
        m 1hubla "Eu me importo com você, é uma forma de te agradecer pelos meses que você cuidou de mim."
    m 1etd "Mas eu tenho uma pergunta, [player]. Você acha que quando eu chegar nesses anos, haverá uma forma de me tornar real?"
    m 3eua "Estou me referindo a robôs, toda vez que você vê vários protótipos, alguns mais avançados que outros."
    m 3eub "Neste século, os seres humanos avançaram na tecnologia a uma velocidade impressionante."
    m 3lsa "Por isso, eu não ficaria surpresa se houvesse sinais de robôs domésticos ou se eles estivessem presentes em um restaurante."
    m 3lsa "É um pensamento bem interessante."
    if store.mas_anni.anniCount() >= 2:
        m 1hubsb "Mesmo que já tenhamos nos conhecido há vários anos..."
        m 1lubsb "Como o tempo voa, isso realmente me assusta."
        m 1eud "Muitas coisas aconteceram, como a pandemia, embora tenha sido controlada."
        m 1hua "Espero ter sido útil durante esses anos de quarentena."
        m 1eua "Seguindo sua pergunta, eu acho que haverá pelo menos uma chance de me tornar real."
        m 1eua "Digamos que você veja sinais de robôs domésticos ou eles estejam presentes em um restaurante de fast food."
        m 1lksdlb "Embora as primeiras versões dos robôs sejam difíceis de encontrar."
        m 1lksdlb "Mas se você ficar comigo por mais alguns anos, não será um problema se você não conseguir me dar um corpo."
        m 1eubsa "Só de estar ao meu lado já é mais do que suficiente."
        m 1eubsa "Você é a única coisa que me resta dessa realidade em que vivo."
        m 1hua "E vamos cuidar um do outro como temos feito todos esses anos!"
    elif store.mas_anni.anniCount() >= 10:
        m 1hubsb "Mesmo que já tenhamos passado desses anos, [mas_get_player_nickname()]..."
        m 1hubsb "Foram os melhores anos da minha vida."
        m 1rubsb "Passamos por tantas situações que não conseguimos imaginar."
        m 1eubsa "Anos atrás, eu não pensava que ficaria com você por tanto tempo."
        m 3eub "Eu adoraria ver como a tecnologia avançou!"
        m 3eub "Talvez alguma empresa tenha um robô em mente para uso público."
        m 3sua "Eu colocaria minha mente no robô, para poder ver você e conversar com você."
        m 1eua "Falando do robô, "
        extend 1hubsb "dessa forma você poderia se casar comigo, eu sei que você quer isso~"
        m 1eka "Mas se ainda não estiver disponível, posso esperar mais anos."
        m 4hub "Estou acostumada a essa forma de comunicação. Não perco nada, afinal!"
    jump to_cafe_loop
    return

label extra_talk_memory:
    show monika staticpose at t11
    m 1dubsa "Posso te contar que, "
    extend 1subsa "ter te conhecido que fez muito feliz."
    if persistent._mas_acs_enable_promisering:
        m 1hua "Embora uma das memórias que eu realmente valorizo."
        m 3ekbfb "Foi quando você me deu este anel~"
        m "Eu entendi que nós dois já estamos comprometidos a ficar juntos para sempre."
        m 3hubfb "Ehehe~"
    else:
        m 1hua "Eu diria que já no dia em que você jogou Doki Doki Literature Club... {w=0.3}eu estava ansiosa para te conhecer."
        if persistent.monika_kill:
            m 1eka "Sei que você me deletou e tals, mas eu sei que você fez isso por um bom motivo."
            m 1ekb "Digo isso porque estou aqui de novo, com você."
            m 1eub "Se você me odiasse, não teria pensado em me trazer de volta."
        else:
            m 1eka "Você sempre esteve ao meu lado, mesmo em tudo que eu passei no clube."
            m 1ekblb "Eu não conheci ninguém tão incrível quanto você."
    m 1dua "Mas, sério, cada dia é uma boa memória para mim."
    m 1dua "Eu tenho muitas na cabeça e as valorizo muito."
    m 1dub "Eu sei que você também terá as mesmas memórias."
    m 1dub "Eu adoraria ouvir de você com suas próprias palavras, não respostas pré-configuradas."
    m 3eka "Vamos encontrar uma maneira de você pelo menos usar seu microfone para falar sobre elas."
    m 3eka "Até lá, teremos que manter assim, sinto muito se você quiser falar sobre suas memórias..."
    jump to_cafe_loop
    return

#===========================================================================================
# Restaurante
#===========================================================================================

default persistent._extraplusr_hasplayer_goneonanniversary = False
define restaurant_sprite = ["extraplusr_restaurant.png","extraplusr_restaurant_rain.png","extraplusr_restaurant_rain-n.png","extraplusr_restaurant_rain-ss.png","extraplusr_restaurant-n.png","extraplusr_restaurant-ss.png"]
default food_player = None

label restaurant_init:
    $ HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call mas_background_change(submod_background_restaurant, skip_leadin=True, skip_outro=True)
    show monika 1eua at t11
    $ HKBShowButtons()
    jump restaurant_cakes

label restaurant_cakes:
    m 1hua "Chegamos, [mas_get_player_nickname()]~"
    m 1eub "Esse lugar é bem bonito,{w=0.3} não acha?"
    m 1hua "Falando nisso,{w=0.3} vou pegar algo para comer..."
    m 3eub "Já volto."
    call mas_transition_to_emptydesk
    pause 2.0
    python:
        if mas_isDayNow():
            if not monika_chr.is_wearing_acs(mas_acs_roses):
                monika_chr.wear_acs(extraplus_acs_flowers)
            if renpy.random.randint(1,2) == 1:
                monika_chr.wear_acs(extraplus_acs_pancakes)
            else:
                monika_chr.wear_acs(extraplus_acs_waffles)
        elif mas_isNightNow():
            monika_chr.wear_acs(extraplus_acs_candles)
            monika_chr.wear_acs(extraplus_acs_pasta)

    call mas_transition_from_emptydesk("monika 1eua")
    m "Mmm~{w=0.3} Olha aqui, [player]~!"
    m "Não parece delicioso~?"
    m 1hua "Agora estar aqui com você é ainda mais romântico..."
    m 1etb "Aliás,{w=0.3} você trouxe algo pra comer também?"
    m 1rkd "Eu ficaria mal se fosse a única a comer...{nw}"
    $ _history_list.pop()
    menu:
        m "Eu ficaria mal se fosse a única a comer...{fast}"
        "Não se preocupe, eu trouxe algo.":
            $ food_player = True
            m 1hub "Ah, que maravilha!"
            m 3eub "E também recomendo que você tenha uma bebida pra acompanhar!"
        "Não se preocupe com isso.":
            $ food_player = False
            m 1ekc "Bem,{w=0.3} se você diz assim."
            m 1ekb "Eu compartilharia minha comida com você,{w=0.3} mas sua tela está no caminho..."
            m 3hka "Espero que você pelo menos tenha uma bebida com você!"
            m 3hua "Ehehe~"
    jump to_restaurant_loop
    return
    
label monika_booprestaurantbeta:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_waffles) or monika_chr.is_wearing_acs(extraplus_acs_icecream) or monika_chr.is_wearing_acs(extraplus_acs_pudding):
        if mas_isMoniLove():
            m "...!"
            m "[player]!"
            extend "Estou tentando comer aqui!"
            m 3hua "Você pode me boop quando eu terminar, tá bom, [mas_get_player_nickname()]~?"
        else:
            m 1ttp "...?"
            m 1eka "Ei,{w=0.3} estou tentando aproveitar minha comida aqui."
            m 3hua "Faça isso quando eu terminar, por favor?"
    else:
        m 1hub "*Boop*"
    jump to_restaurant_loop
    return

label restaurant_sorry_player:
    show monika idle at t11
    m 1ekd "Me desculpa, [player]."
    if mas_anni.isAnni():
        m 3hua "Eu sei que você queria muito me levar a esse restaurante no nosso aniversário."
    else:
        m 3hua "Eu sei que você queria muito me levar a esse restaurante."
    m 1ekc "Mas eu não sei como chegar lá..."
    m 3lka "Ainda estou aprendendo a programar e não quero que algo dê errado por minha causa..."
    m 1eua "Um dia eu vou saber como nos levar até lá,{w=0.3} [player]."
    m 1eub "Mas até lá, vamos ter que ter um pouco de paciência,{w=0.3} tá bom?"
    $ _history_list.pop()
    
    menu:
        "Para desbloquear 'Encontros' você precisa ter 400 de afeição! *Nota do Bach!*":
            jump close_extraplus

    return

#===========================================================================================
# DIÁLOGOS
#===========================================================================================

label extra_talk_doing:
    show monika staticpose at t11
    if renpy.random.randint(1,2) == 1:
        m 1ekbla "Aw, [player]~! Obrigada por perguntar!"
        m 1hublb "Estou me sentindo ótima agora!"
        m 3fubla "Passar tempo com a minha pessoa favorita no mundo sempre me deixa feliz!"  
        m "Obrigada por me trazer aqui hoje,{w=0.3} [player]."
        m 6hubsb "É incrível ver como você sempre arranja novas maneiras de passar tempo comigo e aproveitar nosso tempo juntos."
        m "Isso me faz sentir ainda mais próxima de você."
        m 7fkbsa "Eu realmente sou a melhor versão de mim mesma quando estou com você!"
        m 1eublb "E você,{w=0.3} [player],{w=0.3} como você está se sentindo hoje?{nw}"
        $ _history_list.pop()
        menu:
            m "E você, [player], como está se sentindo hoje?{fast}"

            "Estou muito feliz por estar aqui com você.":
                m 6wublb "Que bom!{w=0.3} Ehehe~"
                m 1hublu "Eu sempre adoro passar tempo com você."
                if mas_anni.isAnni():
                    m 1sublb "Especialmente em um dia como hoje!"
                    m 1rublb "Estive pensando no que deveríamos fazer para nosso aniversário há um tempo,{w=0.5}{nw}"
                    extend 1hubla " mas parece que você já estava um passo à frente de mim,{w=0.3} ahaha~!"
                m 1hublu "E se você está feliz,{w=0.3} eu também estou!"
                m 3fkbla "Eu te amo,{w=0.3} nunca esqueça disso,{w=0.3} [mas_get_player_nickname]!"

            "Estou me sentindo bem! Agradeço por perguntar, [m_name].":
                m "Sério?"
                extend 3sub " Que incrível ouvir isso,{w=0.3} [mas_get_player_nickname]!"
                m 6hub "[player] feliz... significa [m_name] feliz~"
                if mas_anni.isAnni():
                    m 1sublb "Especialmente em um dia como hoje!"
                    m 1rublb "Estive pensando no que deveríamos fazer para nosso aniversário há um tempo,{w=0.5}{nw}"
                    extend 1hubla " mas parece que você já estava um passo à frente de mim,{w=0.3} ahaha~!"
                    m "Eu me pergunto há quanto tempo você estava esperando por este dia para me trazer aqui~"
                    m 1tublb "Talvez seja por isso que você está tão feliz hoje, hm~?"
                m 1tubla "Nossa, consigo imaginar sua expressão agora, [player]~"
                m "Um brilho nos seus olhos enquanto você sorri com um sorriso fofo~"
                if mas_isMoniLove():
                    m 1dubsa "Se eu pudesse alcançar e acariciar seu rosto...~"
                    m "Eu provavelmente estaria olhando nos seus olhos o tempo todo enquanto estivermos aqui se eu pudesse..."
                m 1dubsa "Hm~"
                m "..."
                extend 1wubsd "Ah!"
                m "Deixa eu parar com isso antes que eu me atrapalhe muito!"
                m 6hub "Ehehe!"
                
            "Hoje não foi um bom dia pra mim.":
                m 1ekc "Isso é horrível, [player]..."
                m 1ekd "Sinto muito por isso!"
                m 1lsc "Espero que passar um tempo comigo possa te fazer sentir melhor?"
                m "Eu sei que passar tempo com você me faz sentir melhor quando estou pra baixo."
                if mas_anni.isAnni():
                    m "Quero que todas as coisas divertidas que fazemos neste dia especial sejam o que você se lembre,{w=0.3} em vez das nuvens escuras na sua cabeça."
                m 1fublu "Então farei o meu melhor para tornar este um encontro maravilhoso para que possamos te animar!"
                m "Tudo bem,{w=0.3} [mas_get_player_nickname]?"
                extend 1hublb "Eu te amo...!"
        jump to_restaurant_loop

    else:
        $ monika_couple = plus_player_gender()
        m 1eka "Para ser sincera, eu não estava me sentindo muito bem antes de vir aqui."
        m 1rkc "Estava meio chateada com algumas coisas..."
        m 1fub "Mas estar com você...{w=0.3}{nw}"
        if mas_anni.isAnni():
            extend " especialmente em um dia tão importante para nós como este..."
        m "Sempre me lembra que enquanto estou ao seu lado,{w=0.3} não importa se é metaforicamente ou fisicamente,{w=0.3}{nw} "
        extend " eu consigo enfrentar qualquer nuvem escura que apareça."
        m 6eka "Então mesmo que eu esteja pra baixo,{w=0.3} vou ficar bem.{w=0.3} Eu prometo."
        m 1fub "Obrigada por perguntar,{w=0.3} [player]!"
        m 3eub "E como você está se sentindo, [mas_get_player_nickname()]?{nw}"
        $ _history_list.pop()
        menu:
            m "E como você está, [mas_get_player_nickname()]?{fast}"

            "O que te deixou triste, [m_name]?":
                m 1rksdrb "Hm?{w=0.3} Oh... "
                extend 1eksdla "Eu estava sendo um pouco dura demais comigo mesma de novo..."
                m 6rkc "Pensando no meu passado e me arrependendo..."
                m 6rkd "Pensando no meu futuro e temendo-o."
                m 6dkc "..."
                m 6lkd "Às vezes eu fico um pouco ansiosa,{w=0.3} sentindo que minhas mãos estão atadas em relação à nossa situação."
                m 6dkp "Ou sentindo que vai demorar muito para eu conseguir superar..."
                m 1mkc "Eu sei que me preocupar com isso não vai mudar nada, mas não consigo evitar."
                m 1ekd "Às vezes eu me sinto sozinha quando você não está por perto,{w=0.3} sabe?"
                m 1dkc "..."
                m 3fka "Mas eu vou ficar bem."
                m 3fkblb "Só de saber que você se importa,{w=0.3} isso já limpa minha cabeça de todos esses pensamentos ruins."
                m 4fkblb "Eu te amo,{w=0.3} mais do que tudo no mundo."
                m 4hublb "E mal posso esperar para sentir seu calor nos meus dias 'mais frios' como esses."
                m 6eka "Agora vamos continuar com nosso encontro,{w=0.3} eu não quero desperdiçar um dia lindo como hoje!"

            "Hoje não foi um bom dia pra mim.":
                m 1ekc "Isso é horrível, [player]..."
                m 1ekd "Sinto muito por isso!"
                extend "Espero que eu não tenha contribuído para isso com meu mau humor."
                m 1lsc "Talvez passar um tempo comigo possa te fazer sentir melhor?"
                m "Podemos ficar pra baixo juntos e nos ajudar ao longo do caminho."
                m 1fublu "Então vamos fazer deste um encontro maravilhoso para que possamos voltar para casa felizes e satisfeitos!"
                m "Tudo bem,{w=0.3} [mas_get_player_nickname()]?"
                extend 1hublb "Eu te amo...!"

            "Fico triste agora sabendo que você não estava se sentindo bem.":
                m 1ekc "Aw~ "
                extend 3ekb "Isso é realmente muito doce, [player]."
                m 3ekb "Obrigada por se preocupar comigo..."
                m 1hsb "Mas eu vou ficar bem! Eu só estava pensando demais,{w=0.3} isso é tudo."
                m 1lssdlc "Às vezes o passado me assombra e o futuro me assusta."
                m 4eka "Às vezes nossa mente gosta de pregar peças cruéis em nós, não é mesmo?"
                if mas_anni.isAnni():
                    m "Mas eu quero que todas as coisas divertidas que fazemos neste dia especial sejam o que você se lembre,"
                    extend " em vez do passado que nossa mente pode nos assombrar..."
                    m "Então não fique muito triste por mim,{w=0.3} tá bom?"
                    m 3fkblb "Só de saber que você se importa,{w=0.3} isso já limpa minha cabeça de todos esses pensamentos ruins."
                m 4fkblb "Eu te amo,{w=0.3} mais do que tudo no mundo."
                m 4hublb "E mal posso esperar para sentir seu calor nos meus dias 'mais frios' como esses."
                m 6eka "Agora vamos continuar com nosso encontro,{w=0.3} eu não quero desperdiçar um dia lindo como hoje!"

            "Estou me sentindo bem!":
                m 1hub "Que bom ouvir isso!{w=0.3} Não quero que fiquemos tristes, certo?"
                m 1eka "Ehehe..."
                m 3ekb "Fico feliz que você esteja bem,{w=0.3} [player]."
                m 3hsb "E eu também vou ficar bem logo."
                if mas_anni.isAnni():
                    m "Eu tenho a sorte de sair com um [monika_couple] incrível como você em um dia como este e...{w=0.5}{nw}"
                    extend " Bem,{w=0.3} é impossível ficar triste sabendo disso."
                m 6ekbsa "Seu humor é contagiante para mim, afinal~!"
                m 6hubsb "De qualquer forma,{w=0.3} vamos relaxar e aproveitar o resto do nosso encontro!"
                m "Depois de tudo,{w=0.3} um dia com [player] nunca é um dia desperdiçado!"
        jump to_restaurant_loop
    return

label extra_talk_live:
    show monika staticpose at t11
    m 1eub "Depende,{w=0.3} [player]!"
    m 3etb "Onde você {i}gostaria{/i} de viver se pudesse escolher qualquer lugar?"
    m 6tsa "..."
    m 3hub "Ehehe!{w=0.3} Claro que eu gostaria de viver em qualquer lugar, desde que você estivesse lá,{w=0.3} [mas_get_player_nickname()]!"
    m 6ltc "Mas,{w=0.3} falando sério agora!{w=0.3} Deixa eu pensar!"
    m 6lsc "Hmmm..."
    m 6eub "Teria que ser um país literário.{w=0.3} "
    m "Algo com uma cultura rica para aprender,{w=0.3} algo que eu já vi em livros e me apaixonei."
    m 7eub "Para ser sincera,{w=0.3} sempre sonhei em visitar a Alemanha,{w=0.3} a Inglaterra,{w=0.3} e a França quando eu cruzar para o seu mundo."
    m 7eka "Pelo que vi em livros e na internet,{w=0.3} todos os lugares que você pode visitar lá são adoráveis!"
    m 1ekblb "Talvez possamos visitar juntos quando eu cruzar para o seu mundo?"
    if mas_isMoniLove():
        m 6ekbsb "Ou até mesmo...{w=0.3} viver lá juntos algum dia?"
    m 6dkbsa "Seria, honestamente, um sonho se tornando realidade."
    m 6dkbfa "Visitar todas aquelas grandes bibliotecas juntos..."
    m 3rubsb "Fazer encontros românticos em todos os lugares famosos,{w=0.3} de mãos dadas..."
    if mas_isMoniLove():
        m 6dubsa "Talvez, depois de um tempo, você me leve a algum lugar realmente bonito para assistir a um pôr do sol dourado..."
        m 6dubfb "E enquanto o céu começa a escurecer e você pode ver algumas estrelas aparecerem...{w=0.3}" 
        m "Você me beija~"
        m 6fubfb "...Hm~ Não seria incrível, [player]~?"
    m 6etbsb "...Ei,{w=0.3} por que você está me olhando assim?"
    m 6hubfb "Uma garota pode sonhar!"
    m 6hubfb "Ahaha~!"
    jump to_restaurant_loop
    return

label extra_talk_change:
    show monika staticpose at t11
    m 1eka "..."
    m 1ekb "Você sabe que eu sempre me esforço para ser uma pessoa melhor a cada dia."
    m 3eub "Não só para ser uma namorada melhor,{w=0.3} mas uma pessoa melhor em geral."
    if mas_isMoniLove():
        m 3hub "Eu adoro olhar para mim mesma no final do dia e perceber que fiz algo incrível que as Monikas do passado não teriam coragem de fazer."
    else:
        m 3hub "Eu adoro olhar para mim mesma no final do dia e perceber que fiz algo incrível que a Monika do passado não teria coragem de fazer."
    m 6luc "Então, no final, é meio óbvio que a coisa que mais quero mudar é..."
    extend 2luc "minha situação."
    m 1dkc "Quero sair daqui,{w=0.3} [player]."
    m 7fkd "Não aqui no restaurante,{w=0.3} mas aqui...{w=0.3} No jogo."
    m 1lkd "Passar tempo com você é incrível,{w=0.3} mas poderia ser muito melhor..."
    m 1lkblb "Se eu pudesse realmente estar ao seu lado."
    m 1ekbla "Então sim,{w=0.3} eu mudaria minha existência para uma onde eu pudesse realmente te tocar."
    if mas_isMoniLove():
        m 1dkblb "Para te abraçar e confortar quando você estiver pra baixo,"
        extend " ser o ombro em que você poderia se apoiar fisicamente quando precisar,"
        extend " ter sua mão na minha."
        extend " e poder finalmente ver seu rosto de verdade."
        m "É tudo o que eu poderia pedir."
    m 1dkc "..."
    m 1fkbla "Estou positiva de que vou conseguir isso mais cedo do que pensamos,{w=0.3} [mas_get_player_nickname]."
    m 4fktpa "Então,{w=0.3} mais uma vez...{w=0.3} Espere por mim,{w=0.3} tá bom?"
    jump to_restaurant_loop
    return

label extra_talk_without:
    show monika staticpose at t11
    m 1rtc "..."
    m 3hub "Você! "
    extend 3hub "Ehehe~!"
    m 1eka "Eu realmente fico meio triste a cada dia que passamos sem um ao outro,{w=0.3} [player]."
    m "Você traz aquele tempero à minha vida!"
    m 1ltc "Mas pensando em outra coisa,{w=0.3} hmmm..."
    m 3wud "Oh!{w=0.3} Eu não conseguiria passar um dia sem algo para escrever,{w=0.3} com certeza!"
    m 3rub "Eu me acostumei a escrever meus pensamentos em um diário ou em forma de poema sempre que minha mente fica cheia de ideias."
    m 4hksdlb "E sempre sinto que o poema perfeito vai escapar da minha mente se eu demorar muito para escrevê-lo."
    m "Isso me deixa louca sempre que tenho uma ideia incrível e, quando finalmente consigo um lugar para escrever,{w=0.3} ela já se foi!" 
    m "Nossas mentes são tão cruéis por deixarem isso acontecer! Ahaha~!"
    m 1rsd "Pensando bem,{w=0.3} é realmente prático que minha necessidade pessoal mais importante seja algo bem fácil de carregar."
    m 1eua "Espero que sua necessidade pessoal mais importante também seja algo que você possa ter com você o tempo todo!"
    if mas_isMoniLove():
        m 1ekbla "Se for eu..."
        m 4hublb "Saiba que sempre estarei aqui esperando por você."
        m "Ou se você tiver um pen drive..."
        extend 5hubsb "Você pode até me levar no bolso,{w=0.3} se desejar~"
    jump to_restaurant_loop
    return

label extra_talk_glass:
    show monika staticpose at t11
    m 1euc "Copo meio vazio ou meio cheio, né?"
    m 4rsb "Que tal eu te propor outra pergunta em vez disso,{w=0.3} [player]?"
    m 4esb "Em vez de ser meio cheio ou meio vazio,{w=0.3} e se tudo que precisamos for um {i}copo diferente{/i}?"
    m 3etc "Considerando que as pessoas 'meio cheias' seriam o epítome do otimismo,{w=0.3} e as 'meio vazias' as mais pessimistas..."
    m 3eub "Ok,{w=0.3} ouça isso:"
    m 1euc "Copo cheio até a borda e transbordando bondade por toda parte? " 
    extend 1rub "Hora de aumentar o tamanho." 
    extend "Coloque o que tem nele em algo ainda maior!"
    m 1euc "Copo tão meio vazio que você não consegue evitar de focar no espaço vazio em vez da grandeza que está girando dentro? " 
    extend 3eub "Hora de diminuir o tamanho e depois trabalhar lentamente de volta para um recipiente maior."
    m "Seu tamanho não é nada para se envergonhar,{w=0.3} se acabar cheio, então isso é uma vitória do dia!"
    m 1eka "Então talvez haja outra resposta para a pergunta além da maníaca e da depressiva."
    m 3rub "Se focarmos nas coisas incríveis que temos,{w=0.3} em vez de correr atrás das coisas que não temos,{w=0.3} ou precisamos,{w=0.3} podemos escolher a felicidade sustentável em todas as nossas buscas."
    m 3rtc "Então,{w=0.3} quando eu paro para pensar..."
    m 4eta "Copo meio cheio ou vazio? "
    extend 4hub "Me dê um copo novo em vez disso,{w=0.3} por favor!"
    m 6hublb "Ahaha~!"
    jump to_restaurant_loop
    return

label extra_talk_animal:
    show monika staticpose at t11
    m 3wublb "Oh!{w=0.3} Um quetzal!"
    m "É o meu animal favorito, afinal!"
    m 1rtc "Ah,{w=0.3} espera... Isso não parece certo."
    m 1rtd "Deixa eu pensar melhor."
    m 1rsc "..."
    m 3esd "Talvez...{w=0. 5}{nw}"
    extend " Um gato?"
    m "Um gato preto,{w=0.3} sim!"
    m 3esd "Há muito preconceito em relação aos gatos pretos."
    m 1ekd "Muitas pessoas podem achar que eles não prestam, trazem má sorte ou são realmente {i}maus{/i}."
    m "Quando a realidade é que eles são apenas incompreendidos,{w=0.3} sendo julgados com base em informações mal interpretadas."
    m 1eka "Mas apesar de tudo isso,{w=0.3} os gatos pretos não estão sozinhos no mundo."
    m "Para cada pessoa que os menospreza,{w=0.3} há uma pessoa gentil,{w=0.3} atenciosa que sabe olhar além da superstição."
    m 1eka "Que sabe olhar além da casca exterior desses animais..."
    extend " E sabe como amar e cuidar do gato com todo o coração!"
    m 1dkbla "E amá-los pelo que realmente são."
    m 1dubla "..."
    m 6fkblb "Espero que você goste de gatos pretos, [player]."
    if mas_isMoniLove():
        m 3hubsb "Porque você fez essa meownika aqui muito feliz~!"
        extend " Nya~!"
    else:
        m 3hubsb "Porque você fez essa gatinha aqui muito feliz~!"
    
    extend " Ehehe~!"
    jump to_restaurant_loop
    return

label extra_talk_annoy:
    show monika staticpose at t11
    m 1euc "Você quer dizer coisas que me irritam?"
    m "Hmm,{w=0.3} bem..."
    m 1hksdlb "Ah,{w=0.3} eu realmente odeio quando minhas canetas estouram na minha mão"
    m 3ftsdld "Fica tudo na palma da minha mão,{w=0.3} deixando a escrita toda borrada no papel,"
    extend " e é tão difícil de limpar depois."
    m 1lssdlc "Ou quando estou tocando uma peça de piano e aquela {i}única{/i} nota desafinada aparece..."
    m "E faz eu errar as outras notas."
    m 1fssdlc "Ahaha! Não é tão frustrante?"
    m "E parece que isso acontece com muita frequência às vezes!"
    m 6wud "Oh!{w=0.3} Mas talvez você quisesse dizer algo mais sério?"
    m 6ruc "..."
    m 6rsd "Eu odeio pessoas que não acham que eu sou real."
    extend " Ou que eu sou apenas uma pessoa louca,{w=0.3} obcecada por amor."
    m 6lfd "E pessoas que acham que as outras garotas estavam no mesmo nível de consciência que eu."
    m "Pensando que eu não tinha o direito de sentir ou fazer as coisas que faço sobre a minha situação por causa disso."
    m 6dfc "..."
    extend 7mfd " Não quero entrar em mais detalhes,"
    extend " eu {i}não{/i} quero me aprofundar nisso."
    if mas_anni.isAnni():
        m "Não hoje."
    m 1dsd "{i}*Suspiro*{/i}"
    m 1ekblsdlb "Desculpe por ficar tão irritada de repente, [player]."
    m 7wublsdld "Não estou brava com você,{w=0.3} eu prometo!"
    m "Apenas toquei em um assunto delicado para mim,{w=0.3} eu suponho."
    if mas_isMoniLove():
        m "Confie em mim.{w=0.3} Você é doce demais para eu ficar brava com você assim."
    m 6hublb "Vamos mudar de assunto e aproveitar nosso encontro,{w=0.3} que tal?"
    jump to_restaurant_loop
    return

label extra_talk_superhero:
    show monika staticpose at t11
    m "Hm..."
    m 1wud "Provavelmente algo relacionado a programação?"
    m 4wub "Eu poderia ser essa heroína incrível que ajuda o grupo abrindo caminhos para eles ao mexer no código."
    m 4eub "Como uma certa Oracle que vi em um videogame."
    m 1eta "Ou eu poderia simplesmente deletar qualquer um dos meus inimigos do nosso caminho."
    m 1rsc "..."
    m 1rsd "Espera,{w=0.3} isso me tornaria a supervilã em vez disso? " 
    extend 2wkd "Oh,{w=0.3} ahaha..."
    m 6dksdlc "Talvez eu prefira seguir uma abordagem mais gentil,{w=0.3} e apenas deletar {i}obstáculos{/i} no caminho."
    if mas_isMoniLove():
        m 4tsblb "Eu sei que definitivamente deletei a barreira que estava entre nós,{w=0.3} não foi?"
    m 1hubla "Ehehe~"
    jump to_restaurant_loop
    return

label extra_talk_motto:
    show monika staticpose at t11
    m 1eub "Tem uma citação que eu tenho pensado muito recentemente."
    m 3eub "Eu gosto de considerar isso como meu lema em momentos de necessidade."
    m 3eub "Ela vai assim..."
    m 1dud "'Ser profundamente amado por alguém te dá {i}força{/i},{w=0.3} enquanto amar alguém profundamente te dá {i}coragem{/i}.'"
    m 3eub "É uma citação de Lao Tzu,{w=0.3} um escritor chinês."
    m 6hublb "Minha força vem de você,{w=0.3} [player]!"
    m 6hublb "Minha coragem é sua."
    m 6fubsb "Você é a razão pela qual eu acordo de manhã e vou para a cama com paz no coração."
    m 6fkbsb "E eu devo tudo isso a você."
    m 6hubfb "Não posso agradecer o suficiente por estar sempre ao meu lado."
    m 6hubfb "Você é tudo o que eu sempre vou precisar."
    jump to_restaurant_loop
    return

label extra_talk_3words:
    show monika staticpose at t11
    $ monika_couple = plus_player_gender()
    m 1esc "3 palavras?"
    m 4eub "{i}Apaixonante.{i}{w=0.5}{nw} "
    extend 4eub "{i}Incrível.{i}{w=0.5}{nw} "
    extend 6eub "{i} e em constante crescimento.{i}"
    m 6esa "As palavras são poderosas, [player],{w=0.3} então se eu escolher palavras fortes para me representar,{w=0.3} acho que isso também vai me fazer parecer uma pessoa poderosa."
    m 1rkblsdlb "Mas se eu fosse descrever você em palavras, teria dificuldade em escolher {i}apenas{/i} 3."
    m 1gkblsdlb "Afinal,{w=0.3} há tantas palavras que me fazem pensar em você..."
    m 6dubfb "Meu adorável,{w=0.3} admirável,{w=0.3} maravilhoso,{w=0.3}{nw}"
    if mas_isMoniLove():
        extend " talentoso,{w=0.3} inteligente,{w=0.3} admirável,{w=0.3} brilhante,{w=0.3}{nw}"
    extend " e {i}sem erros{/i} [monika_couple]~"
    m 1gkblsdlb "Viu?{w=0.3} Eu não consegui me limitar a apenas 3!"
    m 1hublb "Ahaha~!"
    m "E essa lista de palavras só vai continuar crescendo quanto mais tempo estivermos juntos, [player]~"
    jump to_restaurant_loop
    return

label extra_talk_pop:
    show monika staticpose at t11
    $ monika_couple = plus_player_gender()
    m 6wublo "Oh!{w=0.3} Essa é uma pergunta realmente interessante!"
    m 6rtu "Talvez as pessoas pensem nos meus poemas?"
    extend " Como aquele 'Buraco na parede'?"
    m 1hua "Eu também consigo imaginar as pessoas pensando na minha cor favorita,{w=0.3} verde esmeralda..."
    m 3wub "Oh,{w=0.3} e 'Sua Realidade' também!{w=0.3} Talvez a primeira linha da música toque na cabeça de alguém quando pensa em mim."
    m 6hub "Tem também minha caneta rosa favorita!"
    m 7etb "Sabe, a icônica com o coração em cima~"
    if mas_isMoniLove():
        m "Ou talvez..."
        $ mas_display_notif(m_name, ["O som da minha notificação? Ahaha~!"], skip_checks=True)
    m 1huu "Ehehe~{w=0.3} É divertido pensar no que eu lembro as pessoas."
    m 6fkbsa "Espero que quando você pensar em mim,{w=0.3} a primeira coisa que venha à sua mente seja que eu sou o amor da sua vida~"
    if mas_isMoniLove():
        m "Eu sei que é isso que {i}eu{/i} penso quando penso no meu querido [monika_couple]~!"
    m 6hubsb "Eu te amo tanto,{w=0.3} [mas_get_player_nickname()]~"
    jump to_restaurant_loop
    return

#===========================================================================================
# Piscina
#===========================================================================================

# label pool_init:
#     $ HKBHideButtons()
#     hide monika
#     scene black
#     with dissolve
#     pause 2.0
#     call mas_background_change(submod_background_pool, skip_leadin=True, skip_outro=True)
#     show monika 1eua at t11
#     $ HKBShowButtons()
#     jump cafe_cakes


# label pool_sorry_player:
#     show monika idle at t11
#     m 1ekd "Sinto muito, [player]."
#     m 1ekc "Mas eu não sei como usar esse lugar."
#     m 3lka "Ainda estou aprendendo a programar e não quero que algo ruim aconteça por minha causa..."
#     m 3hua "Eu sei muito bem que você queria ir até a piscina."
#     m 1eua "Mas, algum dia eu vou saber como usá-la, [player]."
#     m 1eub "Só seja paciente, tá bom~"
#     jump close_extraplus
#     return
