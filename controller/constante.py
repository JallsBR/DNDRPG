from random import randint

nd_livro = [
    {'ND': '0', 'Proef': 2, "CA": 13, 'PV': randint(1, 6), 'Pvmin': 1, 'Pvmax': 6, 'Bônus Ataque': 3,
        'Dano Rodada': randint(0, 1), 'Danomin': 0, 'Danomax': 1, 'CD': 13, 'XP': 10},
    
    {'ND': '1/8', 'Proef': 2, "CA": 13, 'PV': randint(7, 35), 'Pvmin': 7, 'Pvmax': 35, 'Bônus Ataque': 3,
        'Dano Rodada': randint(2, 3), 'Danomin': 2, 'Danomax': 3, 'CD': 13, 'XP': 25},
    
    {'ND': '1/4', 'Proef': 2, "CA": 13, 'PV': randint(36, 49), 'Pvmin': 36, 'Pvmax': 49, 'Bônus Ataque': 3,
        'Dano Rodada': randint(4, 5), 'Danomin': 4, 'Danomax': 5, 'CD': 13, 'XP': 50},
    
    {'ND': '1/2', 'Proef': 2, "CA": 13, 'PV': randint(50, 70), 'Pvmin': 50, 'Pvmax': 70, 'Bônus Ataque': 3,
        'Dano Rodada': randint(6, 8), 'Danomin': 6, 'Danomax': 8, 'CD': 13, 'XP': 100},
    
    {'ND': '1', 'Proef': 2, "CA": 13, 'PV': randint(71, 85), 'Pvmin': 71, 'Pvmax': 85, 'Bônus Ataque': 3,
        'Dano Rodada': randint(9, 14), 'Danomin': 9, 'Danomax': 14, 'CD': 13, 'XP': 200},
    
    {'ND': '2', 'Proef': 2, "CA": 13, 'PV': randint(86, 100), 'Pvmin': 86, 'Pvmax': 100, 'Bônus Ataque': 3,
        'Dano Rodada': randint(15, 20), 'Danomin': 15, 'Danomax': 20, 'CD': 13, 'XP': 450},
    
    {'ND': '3', 'Proef': 2, "CA": 13, 'PV': randint(101, 115), 'Pvmin': 101, 'Pvmax': 115, 'Bônus Ataque': 4,
        'Dano Rodada': randint(21, 26), 'Danomin': 21, 'Danomax': 26, 'CD': 13, 'XP': 700},
    
    {'ND': '4', 'Proef': 2, "CA": 14, 'PV': randint(116, 130), 'Pvmin': 116, 'Pvmax': 130, 'Bônus Ataque': 5,
        'Dano Rodada': randint(27, 32), 'Danomin': 27, 'Danomax': 32, 'CD': 14, 'XP': 1100},
    
    {'ND': '5', 'Proef': 3, "CA": 15, 'PV': randint(131, 145), 'Pvmin': 131, 'Pvmax': 145, 'Bônus Ataque': 6,
        'Dano Rodada': randint(33, 38), 'Danomin': 33, 'Danomax': 38, 'CD': 15, 'XP': 1800},
    
    {'ND': '6', 'Proef': 3, "CA": 15, 'PV': randint(146, 160), 'Pvmin': 146, 'Pvmax': 160, 'Bônus Ataque': 6,
        'Dano Rodada': randint(39, 44), 'Danomin': 39, 'Danomax': 44, 'CD': 15, 'XP': 2300},
    
    {'ND': '7', 'Proef': 3, "CA": 15, 'PV': randint(161, 175), 'Pvmin': 161, 'Pvmax': 175, 'Bônus Ataque': 6,
        'Dano Rodada': randint(45, 50), 'Danomin': 45, 'Danomax': 50, 'CD': 15, 'XP': 2900},
    
    {'ND': '8', 'Proef': 3, "CA": 16, 'PV': randint(176, 190), 'Pvmin': 176, 'Pvmax': 190, 'Bônus Ataque': 7,
        'Dano Rodada': randint(51, 56), 'Danomin': 51, 'Danomax': 56, 'CD': 16, 'XP': 3900},
    
    {'ND': '9', 'Proef': 4, "CA": 16, 'PV': randint(191, 205), 'Pvmin': 191, 'Pvmax': 205, 'Bônus Ataque': 7,
        'Dano Rodada': randint(57, 62), 'Danomin': 57, 'Danomax': 62, 'CD': 16, 'XP':5000 },
    
    {'ND': '10', 'Proef': 4, "CA": 17, 'PV': randint(206, 220), 'Pvmin': 206, 'Pvmax': 220, 'Bônus Ataque': 7,
        'Dano Rodada': randint(63, 68), 'Danomin': 63, 'Danomax': 68, 'CD': 16, 'XP': 5900},
    
    {'ND': '11', 'Proef': +4, "CA": 17, 'PV': randint(221, 235), 'Pvmin': 221, 'Pvmax': 235,
        'Bônus Ataque': 8, 'Dano Rodada': randint(69, 74), 'Danomin': 69, 'Danomax': 74, 'CD': 17, 'XP': 7200},
    
    {'ND': '12', 'Proef': +4, "CA": 17, 'PV': randint(236, 250), 'Pvmin': 236, 'Pvmax': 250,
        'Bônus Ataque': 8, 'Dano Rodada': randint(75, 80), 'Danomin': 75, 'Danomax': 80, 'CD': 17, 'XP': 8400},
    
    {'ND': '13', 'Proef': +5, "CA": 18, 'PV': randint(251, 265), 'Pvmin': 251, 'Pvmax': 265,
        'Bônus Ataque': 8, 'Dano Rodada': randint(81, 86), 'Danomin': 81, 'Danomax': 86, 'CD': 18, 'XP': 10000},
    
    {'ND': '14', 'Proef': +5, "CA": 18, 'PV': randint(266, 280), 'Pvmin': 266, 'Pvmax': 280,
        'Bônus Ataque': 8, 'Dano Rodada': randint(87, 92), 'Danomin': 87, 'Danomax': 92, 'CD': 18, 'XP': 11500},
    
    {'ND': '15', 'Proef': +5, "CA": 18, 'PV': randint(281, 295), 'Pvmin': 281, 'Pvmax': 295,
        'Bônus Ataque': 8, 'Dano Rodada': randint(93, 98), 'Danomin': 93, 'Danomax': 98, 'CD': 18, 'XP': 13000},
    
    {'ND': '16', 'Proef': +5, "CA": 18, 'PV': randint(296, 310), 'Pvmin': 296, 'Pvmax': 310,
        'Bônus Ataque': 9, 'Dano Rodada': randint(99, 104), 'Danomin': 99, 'Danomax': 104, 'CD': 18, 'XP': 15000},
    
    {'ND': '17', 'Proef': +6, "CA": 19, 'PV': randint(311, 325), 'Pvmin': 311, 'Pvmax': 325,
        'Bônus Ataque': 10, 'Dano Rodada': randint(105, 110), 'Danomin': 105, 'Danomax': 110, 'CD': 19, 'XP': 18000},
    
    {'ND': '18', 'Proef': +6, "CA": 19, 'PV': randint(326, 340), 'Pvmin': 326, 'Pvmax': 340,
        'Bônus Ataque': 10, 'Dano Rodada': randint(111, 116), 'Danomin': 111, 'Danomax': 116, 'CD': 19, 'XP': 20000},
    
    {'ND': '19', 'Proef': +6, "CA": 19, 'PV': randint(341, 355), 'Pvmin': 341, 'Pvmax': 355,
        'Bônus Ataque': 10, 'Dano Rodada': randint(117, 122), 'Danomin': 117, 'Danomax': 122, 'CD': 19, 'XP': 22000},
    
    {'ND': '20', 'Proef': +6, "CA": 19, 'PV': randint(356, 400), 'Pvmin': 356, 'Pvmax': 400,
        'Bônus Ataque': 10, 'Dano Rodada': randint(123, 140), 'Danomin': 123, 'Danomax': 140, 'CD': 19, 'XP': 25000},
    
    {'ND': '21', 'Proef': +7, "CA": 19, 'PV': randint(401, 445), 'Pvmin': 401, 'Pvmax': 445,
        'Bônus Ataque': 11, 'Dano Rodada': randint(141, 158), 'Danomin': 141, 'Danomax': 158, 'CD': 20, 'XP': 33000},
    
    {'ND': '22', 'Proef': +7, "CA": 19, 'PV': randint(446, 490), 'Pvmin': 446, 'Pvmax': 490,
        'Bônus Ataque': 11, 'Dano Rodada': randint(159, 176), 'Danomin': 159, 'Danomax': 176, 'CD': 20, 'XP': 41000},
    
    {'ND': '23', 'Proef': +7, "CA": 19, 'PV': randint(491, 535), 'Pvmin': 491, 'Pvmax': 535,
        'Bônus Ataque': 11, 'Dano Rodada': randint(177, 194), 'Danomin': 177, 'Danomax': 194, 'CD': 20, 'XP': 50000},
    
    {'ND': '24', 'Proef': +7, "CA": 19, 'PV': randint(536, 580), 'Pvmin': 536, 'Pvmax': 580,
        'Bônus Ataque': 11, 'Dano Rodada': randint(195, 212), 'Danomin': 195, 'Danomax': 212, 'CD': 21, 'XP': 62000},
    
    {'ND': '25', 'Proef': +8, "CA": 19, 'PV': randint(581, 625), 'Pvmin': 581, 'Pvmax': 625,
        'Bônus Ataque': 12, 'Dano Rodada': randint(213, 230), 'Danomin': 213, 'Danomax': 230, 'CD': 21, 'XP': 75000},
    
    {'ND': '26', 'Proef': +8, "CA": 19, 'PV': randint(626, 670), 'Pvmin': 626, 'Pvmax': 670,
        'Bônus Ataque': 12, 'Dano Rodada': randint(231, 248), 'Danomin': 231, 'Danomax': 248, 'CD': 21, 'XP': 90000},
    
    {'ND': '27', 'Proef': +8, "CA": 19, 'PV': randint(671, 715), 'Pvmin': 671, 'Pvmax': 715,
        'Bônus Ataque': 13, 'Dano Rodada': randint(249, 266), 'Danomin': 249, 'Danomax': 266, 'CD': 22, 'XP': 105000},
    
    {'ND': '28', 'Proef': +8, "CA": 19, 'PV': randint(716, 760), 'Pvmin': 715, 'Pvmax': 760,
        'Bônus Ataque': 13, 'Dano Rodada': randint(267, 284), 'Danomin': 267, 'Danomax': 284, 'CD': 22, 'XP': 120000},
    
    {'ND': '29', 'Proef': +9, "CA": 19, 'PV': randint(761, 805), 'Pvmin': 761, 'Pvmax': 805,
        'Bônus Ataque': 13, 'Dano Rodada': randint(285, 302), 'Danomin': 285, 'Danomax': 302, 'CD': 22, 'XP': 135000},
    
    {'ND': '30', 'Proef': +9, "CA": 19, 'PV': randint(806, 850), 'Pvmin': 806, 'Pvmax': 850,
        'Bônus Ataque': 14, 'Dano Rodada': randint(303, 320), 'Danomin': 303, 'Danomax': 320, 'CD': 23, 'XP': 155000},
    ]

