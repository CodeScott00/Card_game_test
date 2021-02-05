import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
        
    def setUp(self):
        self.card1 = Card("diamonds", 1)
        self.card2 = Card("spades", 3)
        self.cards = [self.card1, self.card2]
        self.game1 = CardGame()

    def test_check_for_ace(self):
       self.assertEqual(True, self.game1.check_for_ace(self.card1))
        
    def test_check_for_ace_false(self):
       self.assertEqual(False, self.game1.check_for_ace(self.card2))
        
    def test_highest_card(self):
        self.assertEqual(self.card2,self.game1.highest_card(self.card1,self.card2))
    
    def test_cards_total(self):
        result = self.game1.cards_total(self.cards) 
        self.assertEqual("You have a total of 4", result)




