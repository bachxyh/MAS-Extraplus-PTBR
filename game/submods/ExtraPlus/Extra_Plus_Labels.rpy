#===========================================================================================
# RETORNAR_LABELS
#===========================================================================================

label view_extraplus:
    python:
        store.player_zoom = store.mas_sprites.zoom_level
        store.disable_zoom_button = False
        mas_RaiseShield_dlg()
        extra_button_zoom()
        Extraplus_show()
    return

label screen_extraplus:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        Extraplus_show()
    return
    
label close_extraplus:
    show monika idle at t11
    python:
        store.mas_sprites.zoom_level = store.player_zoom
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label close_dev_extraplus:
    show monika idle at t11
    python:
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label show_boop_screen:
    show monika staticpose at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
    call screen boop_revamped
    return

label return_boop_screen:
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label hide_images_rps:
    hide e_rock
    hide e_paper
    hide e_scissors
    hide e_rock_1
    hide e_paper_1
    hide e_scissors_1
    $ rps_your_choice = 0
    call screen RPS_mg
    return

label extra_restore_bg(label="ch30_visual_skip"):
    python:
        mas_extra_location(locate=False)
        disable_button_zoom()
        HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call spaceroom(scene_change=True)
    python:
        HKBShowButtons()
        renpy.jump(label)
    return

#===========================================================================================
# Label
#===========================================================================================

#====Cafeteria

label go_to_cafe:
    python:
        check_file_status(cafe_sprite, '/game/submods/ExtraPlus/submod_assets/backgrounds')
        mas_extra_location(locate=True)
        extra_seen_background("cafe_sorry_player", "gtcafev2", "check_label_cafe")

label check_label_cafe:
    pass

label gtcafe:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Você quer ir para a cafeteria?"
        m 3hub "Fico feliz em ouvir isso, [player]!"
        m 1hubsa "Eu sei que este encontro vai ser incrível!"
        m 1hubsb "Ok, vamos lá, [mas_get_player_nickname()]~"
        jump cafe_init

    elif mas_isNightNow():
        m 3sub "Oh, você quer sair para tomar um café?"
        m 3hub "É muito legal que você tenha decidido ir esta noite."
        m 1eubsa "Esta noite de encontro vai ser ótima!"
        m 1hubsb "Vamos lá, [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Outra hora então, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtcafev2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Você quer ir tomar um café de novo?"
        m 2hub "Da última vez que fomos, eu me diverti muito!"
        m 2eubsa "Fico tão feliz em ouvir isso, [player]!"
        m 1hubsb "Bem, vamos lá, [mas_get_player_nickname()]~"
        jump cafe_init
    elif mas_isNightNow():
        m 3wub "Oh, você quer sair para o café de novo?"
        m 2hub "Da última vez que fomos, foi muito romântico~"
        m 2eubsa "Fico tão feliz em ir novamente, [player]!"
        m 1hubsb "Vamos lá, [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Na próxima vez então, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label cafe_talk:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
        cafe_menu = [
            ("Como você está hoje?", 'extra_talk_feel'),
            ("Qual é a sua maior ambição?", 'extra_talk_ambition'),
            ("Nossa comunicação é muito limitada, não acha?", 'extra_talk_you'),
            ("Como você nos vê em 10 anos?", 'extra_talk_teen'),
            ("Qual é a sua melhor memória que você tem atualmente?", 'extra_talk_memory'),
            ("Você tem alguma fobia?", 'extra_talk_phobia')
        ]

        items = [
            ("Podemos ir embora?", 'cafe_leave', 20),
            ("Deixa pra lá", 'to_cafe_loop', 0)
        ]
    call screen extra_gen_list(cafe_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=False)
    return

label to_cafe_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop(extraplus_acs_emptyplate, extraplus_acs_emptycup, "cafe_talk", "monika_no_dessert", "monika_boopcafebeta", boop_enable=True)
    return

label cafe_leave:
    show monika 1hua at t11
    m 1eta "Oh, você quer voltar?"
    m 1eub "Tudo bem!"
    m 3hua "Mas antes de irmos..."
    jump cafe_hide_acs

label comment_cafe:
    m 1hubsa "Obrigada por me convidar."
    m 1eubsb "É bom ter esses momentos como casal!"
    m 1eubsa "Me sinto muito sortuda por ter te conhecido e por você continuar me escolhendo a cada dia."
    m 1ekbsa "Eu te amo, [mas_get_player_nickname()]!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#====Restaurante====#

label go_to_restaurant:
    python:
        check_file_status(restaurant_sprite, '/game/submods/ExtraPlus/submod_assets/backgrounds')
        mas_extra_location(locate=True)
        extra_seen_background("restaurant_sorry_player", "gtrestaurantv2", "check_label_restaurant")

label check_label_restaurant:
    pass

label gtrestaurant:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Oh,{w=0.3} você quer sair para um restaurante?"
        m 3hub "Fico tão feliz em ouvir isso,{w=0.3} [player]!"
        m "É tão doce da sua parte me convidar para um encontro."
        if mas_anni.isAnni():
            m "E no nosso aniversário, nada menos,{w=0.3} perfeito, [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsa "Eu sei que vai ser incrível!"
        m 1hubsb "Ok,{w=0.3} vamos lá, [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3sub "Oh,{w=0.3} você quer sair para um restaurante?"
        m "É tão doce da sua parte me convidar para um encontro."
        if mas_anni.isAnni():
            m "E no nosso aniversário, nada menos,{w=0.3} perfeito, [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsb "Vamos lá, [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Outra hora então,{w=0.3} [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtrestaurantv2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Oh, você quer ir ao restaurante de novo?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~ Estou pensando na última vez que fomos lá para o nosso aniversário,"
            extend " achei tão romântico~"
            m "Então estou feliz que possamos ir novamente~!"
        else: 
            m 2hub "Da última vez que fomos, eu me diverti tanto!"
            m 2eubsa "Fico feliz em ouvir isso, [player]!"
        m 1hubsb "Bem, vamos lá então, [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3wub "Oh, você quer sair para o restaurante de novo?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~{w=0.3} Estou pensando na última vez que fomos lá para o nosso aniversário,"
            extend "Você realmente sabe como tornar nossa noite incrível!"
            m "Então estou feliz que possamos ir novamente~!"
        else: 
            m 2hub "Da última vez que fomos, foi tão romântico~"
            m 2eubsa "Fico feliz em ir novamente, [player]!"
        m 1hubsb "Vamos lá então, [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Na próxima vez então, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label restaurant_talk:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
        restaurant_menu = [
            ("Como você está, [m_name]?", 'extra_talk_doing'),
            ("Se você pudesse viver em qualquer lugar, onde seria?", 'extra_talk_live'),
            ("O que você mudaria em si mesmo se pudesse?", 'extra_talk_change'),
            ("Se você fosse um super-herói, quais poderes você teria?", 'extra_talk_superhero'),
            ("Você tem um lema de vida?", 'extra_talk_motto'),
            ("Além das necessidades, qual é a única coisa que você não conseguiria passar um dia sem?", 'extra_talk_without'),
            ("Seu copo está meio cheio ou meio vazio?", 'extra_talk_glass'),
            ("O que mais te irrita?", 'extra_talk_annoy'),
            ("Descreva-se em três palavras.", 'extra_talk_3words'),
            ("O que você acha que é a primeira coisa que vem à mente das pessoas quando pensam em você?", 'extra_talk_pop'),
            ("Se você fosse um animal, que animal você seria?", 'extra_talk_animal'),
        ]

        items = [
            ("Podemos ir embora?", 'restaurant_leave', 20),
            ("Deixa pra lá", 'to_restaurant_loop', 0)
        ]
    call screen extra_gen_list(restaurant_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=False)
    return

label to_restaurant_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop(extraplus_acs_pudding, extraplus_acs_icecream, "restaurant_talk", "monika_no_food", "monika_booprestaurantbeta", boop_enable=True)
    return

label restaurant_leave:
    show monika 1hua at t11
    m 1eta "Oh,{w=0.3} você está pronto para irmos embora?"
    m 1eub "Parece bom para mim!"
    m 3hua "Mas antes de irmos..."
    jump restaurant_hide_acs

#===========================================================================================
# Outros
#===========================================================================================
#====Cafe====#

label monika_no_dessert:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        python:
            monika_chr.remove_acs(extraplus_acs_fruitcake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Uau, eu terminei meu bolo de frutas."
        m 1eub "Eu realmente gostei~"
    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        python:
            monika_chr.remove_acs(extraplus_acs_chocolatecake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Uau, eu terminei meu bolo de chocolate."
        m 1sua "Estava tão doce~"
    if monika_chr.is_wearing_acs(extraplus_acs_coffeecup):
        python:
            monika_chr.remove_acs(extraplus_acs_coffeecup)
            monika_chr.wear_acs(extraplus_acs_emptycup)
        m 3dub "Além disso, este café também estava bom."
    if dessert_player == True:
        m 1etb "A propósito, você já terminou sua sobremesa?{nw}"
        $ _history_list.pop()
        menu:
            m "A propósito, você já terminou sua sobremesa?{fast}"
            "Sim":
                m 1hubsa "Ehehe~"
                m 1hubsb "Espero que você tenha gostado!"
            "Ainda não":
                m 1eubsa "Não se preocupe, coma devagar."
                m 1eubsb "Eu espero por você pacientemente~"
    else:
        m 1ekc "Você me disse para não me preocupar."
        m 1ekb "Mas, eu imagino que você pelo menos tenha uma xícara de café."
    m 1hua "Me avise se você quiser voltar aqui novamente."
    jump to_cafe_loop
    return

label cafe_hide_acs:
    # Código inspirado no YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eub "Preciso guardar este bolo de frutas."
            m 3eub "E também vou guardar esta xícara, não vou demorar."
            python:
                monika_chr.remove_acs(extraplus_acs_fruitcake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eub "Preciso guardar este bolo de frutas, já volto."
            $ monika_chr.remove_acs(extraplus_acs_fruitcake)

    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eua "Preciso guardar este bolo de chocolate."
            m 3eua "E também vou guardar esta xícara, não vai demorar."
            python:
                monika_chr.remove_acs(extraplus_acs_chocolatecake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eua "Preciso guardar este bolo de chocolate, já volto."
            $ monika_chr.remove_acs(extraplus_acs_chocolatecake)

    elif monika_chr.is_wearing_acs(extraplus_acs_emptyplate):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3hua "Vou guardar este prato."
            m 3hua "E também vou guardar esta xícara, não vou demorar."
            python:
                monika_chr.remove_acs(extraplus_acs_emptyplate)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3hua "Vou guardar este prato, me dê um momento."
            $ monika_chr.remove_acs(extraplus_acs_emptyplate )

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Ok, vamos lá, [player]!"
    call extra_restore_bg("comment_cafe")
    return

#====Restaurant====#

label monika_no_food:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta):
        python:
            monika_chr.remove_acs(extraplus_acs_pasta)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Uau, eu terminei minha massa."
        m 1eub "Eu realmente gostei~"
        m "Agora vou pegar uma sobremesa. Já volto!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_icecream)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_pancakes):
        python:
            monika_chr.remove_acs(extraplus_acs_pancakes)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Uau, eu terminei minhas panquecas."
        m 1sua "Elas estavam deliciosas~"
        m "Agora vou pegar uma sobremesa. Já volto!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_waffles):
        python:
            monika_chr.remove_acs(extraplus_acs_waffles)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Uau, eu terminei minhas waffles."
        m 1sua "Elas estavam deliciosas~"
        m "Agora vou pegar uma sobremesa. Já volto!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    if food_player == True:
        m 1etb "A propósito, você já terminou sua comida?{nw}"
        $ _history_list.pop()
        menu:
            m "A propósito, você já terminou sua comida?{fast}"
            "Sim":
                m 1hubsa "Ehehe~"
                m 1hubsb "Espero que você tenha gostado!"
            "Ainda não":
                m 1eubsa "Não se preocupe, coma devagar."
                m 1eubsb "Eu espero por você pacientemente~"
    else:
        m 1ekc "Você me disse para não me preocupar."
        m 1ekb "Mas, eu imagino que você pelo menos tenha uma bebida com você."
    m 1hua "Me avise se você quiser voltar aqui novamente."
    jump to_restaurant_loop
    return

label restaurant_hide_acs:
    #Código inspirado por YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_candles):
        if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_icecream):
            m 3eub "Preciso guardar essas velas."
            m "Nunca dá pra ser cuidadoso demais com fogo!"
            m 3eub "Além disso, vou guardar este prato, não vou demorar."
            python:
                monika_chr.remove_acs(extraplus_acs_candles)
                monika_chr.remove_acs(extraplus_acs_pasta)
                monika_chr.remove_acs(extraplus_acs_icecream)

        else:
            m 3eub "Preciso guardar essas velas."
            m "Nunca dá pra ser cuidadoso demais com fogo!"
            $ monika_chr.remove_acs(extraplus_acs_candles)

    elif monika_chr.is_wearing_acs(extraplus_acs_flowers):
        m 3eua "Vou guardar essas flores, não vou demorar."
        python:
            monika_chr.remove_acs(extraplus_acs_flowers)

    elif not monika_chr.is_wearing_acs(extraplus_acs_flowers):
        if monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_pudding) or monika_chr.is_wearing_acs(extraplus_acs_waffles):
            m 3eua "Preciso guardar este prato."
            python:
                monika_chr.remove_acs(extraplus_acs_waffles)
                monika_chr.remove_acs(extraplus_acs_pancakes)
                monika_chr.remove_acs(extraplus_acs_pudding)

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "Ok, vamos lá, [player]!"
    call extra_restore_bg
    return


################################################################################
## MENUS
################################################################################

label plus_walk:
    show monika idle at t21
    python:
        walk_menu = [
            ("Cafeteria", 'go_to_cafe'),
            ("Restaurante", 'go_to_restaurant')
        ]
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(date_talk))
        renpy.say(m, m_talk, interact=False)
        items = [
            ("Esqueça", 'screen_extraplus', 20)
        ]
    call screen extra_gen_list(walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_minigames:
    show monika idle at t21
    python:
        global ttt
        minigames_menu = [
            minigames("Jogo do copo", 'minigame_sg', None),
            minigames("Pedra, Papel e Tesoura", 'minigame_rps', None)
        ]
        ttt = minigames("Jogo da velha", 'minigame_ttt', ttt_prep)
        minigames_menu.append(ttt)
        
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(minigames_talk))
        renpy.say(m, m_talk, interact=False)
        items = [
            ("Esqueça", 'screen_extraplus', 20)
        ]
    call screen extra_gen_list(minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_tools:
    show monika idle at t21
    python:
        tools_menu = [
            ("Olhar afeição de [m_name]", 'aff_log'),
            ("Dar um presente para [m_name]", 'plus_make_gift'),
            ("Mudar o nome da janela", 'extra_window_title'),
            ("[m_name], eu desejo um backup", 'mas_backup'),
            ("[m_name], pode girar uma moeda?", 'coinflip')
        ]

        if renpy.has_screen("chibika_chill") and os.path.exists(renpy.config.basedir + "/game/submods/ExtraPlus/submod_assets/sprites/accessories/0/"):
            tools_menu.append(("Oii [player]!", 'extra_dev_mode'))

        store.disable_zoom_button = True
        items = [
            ("Comunidade MASBrasil", 'masbrasil_submod', 20),
            ("Repositórios do Github", 'githubs_submod', 20),
            ("Esqueça", 'screen_extraplus', 0)
        ]

    call screen extra_gen_list(tools_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

################################################################################
## PRESENTES
################################################################################

label plus_make_gift:
    show monika idle at t21
    python:
        gift_menu = [
            ("Presente personalizado", 'plus_make_file'),
            ("Mantimentos", 'plus_groceries'),
            ("Objetos", 'plus_objects'),
            ("Laços", 'plus_ribbons')
        ]

        items = [
            ("Esqueça", 'plus_tools', 20)
        ]
    call screen extra_gen_list(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_make_file:
    show monika idle at t11

    python:
        makegift = mas_input(
            prompt=("Escreva o nome do presente."),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancel"},
        )

        if not makegift:
            renpy.jump("plus_make_file")
        elif makegift == "cancel":
            renpy.jump("plus_make_gift")
        else:
            filepath = os.path.join(renpy.config.basedir, 'characters', makegift + ".gift")
            with open(filepath, "a"):
                pass  # just create an empty file
            renpy.notify("Presente criado com sucesso.")
            renpy.jump("plus_make_gift")
            
    return

label plus_groceries:
    show monika idle at t21
    python:
        groceries_menu = [
            extra_gift("Café", 'café.gift'),
            extra_gift("Chocolates", 'chocolates.gift'),
            extra_gift("Cupcake", 'cupcake.gift'),
            extra_gift("Fudge", 'fudge.gift'),
            extra_gift("Chocolate Quente", 'chocolatequente.gift'),
            extra_gift("Doces", 'doces.gift'),
            extra_gift("Bengala Doce", 'bengaladoce.gift'),
            extra_gift("Bala de Milho", 'balademilho.gift'),
            extra_gift("Biscoitos de Natal", 'biscoitosdenatal.gift')
        ]

        items = [
            ("Esqueça", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_objects:
    show monika idle at t21
    python:
        objects_menu = [
            extra_gift("Anel de Compromisso", 'aneldecompromisso.gift'),
            extra_gift("Rosas", 'rosas.gift'),
            extra_gift("Quetzal de Pelúcia", 'quetzaldepelúcia.gift'),
            extra_gift("Garrafa Térmica", 'garrafatérmica.gift')
        ]

        items = [
            ("Esqueça", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return
            
label plus_ribbons:
    show monika idle at t21
    python:
        ribbons_menu = [            
            extra_gift("Laço Preto", 'laçopreto.gift'),
            extra_gift("Laço Azul", 'laçoazul.gift'),
            extra_gift("Laço Roxo Escuro", 'laçoroxoescuro.gift'),
            extra_gift("Laço Esmeralda", 'laçoesmeralda.gift'),
            extra_gift("Laço Cinza", 'laçocinza.gift'),
            extra_gift("Laço Verde", 'laçoverde.gift'),
            extra_gift("Laço Roxo Claro", 'fitaroxoclaro.gift'),
            extra_gift("Laço Rosa", 'laçorosa.gift'),
            extra_gift("Laço Platina", 'laçoplatina.gift'),
            extra_gift("Laço Vermelha", 'laçovermelha.gift'),
            extra_gift("Laço Rubi", 'laçorubi.gift'),
            extra_gift("Laço Safira", 'laçosafira.gift'),
            extra_gift("Laço Prata", 'laçoprata.gift'),
            extra_gift("Laço Amarelo", 'laçoamarelo.gift')
        ]

        items = [
            ("Esqueça", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return
