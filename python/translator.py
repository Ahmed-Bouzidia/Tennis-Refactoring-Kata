# -*- coding: utf-8 -*-

class Translator:
    translations = {
        "Love": {"fr": "Zéro"},
        "Fifteen": {"fr": "Quinze"},
        "Thirty": {"fr": "Trente"},
        "Forty": {"fr": "Quarante"},
        "All": {"fr": "À"},
        "Deuce": {"fr": "Égalité"},
        "Advantage player1": {"fr": "Avantage joueur 1"},
        "Advantage player2": {"fr": "Avantage joueur 2"},
        "Win for player1": {"fr": "Victoire pour le joueur 1"},
        "Win for player2": {"fr": "Victoire pour le joueur 2"}
    }

    @classmethod
    def translate(cls, string, lang):
        if string in cls.translations:
            if lang in cls.translations[string]:
                return cls.translations[string][lang]
        return string


 