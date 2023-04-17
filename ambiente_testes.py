def caracteristicas_animal():
    caracteristicas = {'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'},
                                      'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}},
                       'invertebrado': {'inseto': {'hematofago': 'pulga', 'herbivoro': 'lagarta'},
                                        'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}}
    return caracteristicas


def animal():
    for cont1 in range(1):
        caracteristica = str(input())
        tipo_animal = caracteristicas_animal()[caracteristica]

        for cont2 in range(1):
            caracteristica = str(input())
            tipo_animal = tipo_animal[caracteristica]

            for cont3 in range(1):
                caracteristica = str(input())
                tipo_animal = tipo_animal[caracteristica]
                print(tipo_animal)


animal()
