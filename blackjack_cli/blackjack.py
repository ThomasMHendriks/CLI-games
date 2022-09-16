'''
Simple blackjack game
By: Thomas Hendriks
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# Playing cards
class Card():
    
    def __init__(self,suit,rank):
        #Attributes of the cards
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        #Print the specifics of a card
        return self.rank + " of " + self.suit

# Deck to be drawn off
class Deck():
    
    def __init__(self):
        #For loop to create deck of 52 cards
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.deck.append(new_card)
    
    def __str__(self):
        #print the full deck when called
        full_deck = ""
        for x in range(len(self.deck)):
            full_deck += str(self.deck[x]) + "\n"
        return full_deck
        
    def shuffle(self):
        #shuffle the created deck
        random.shuffle(self.deck)
    
    def deal(self):
        #Remove a card from the deck
        return self.deck.pop()

# Keep track of cards in hand
class Hand():
    
    def __init__(self):
        #start values for an empty hand
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        #Add the drawn card to hand
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        #Switch an ace value from 11 to 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
    def __str__(self):
        #print the full hand when called
        full_hand = ""
        for x in range(len(self.cards)):
            full_hand += str(self.cards[x]) + "  "
        return full_hand

#  Keeps track of the chip stack of the player
class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# Take in the desired player bet
def take_bet(chips):
    bet_required = True
    
    while bet_required:
        try:
            chips.bet = int(input("How many chips do you want to bet: "))            
        except:
            print("That is not valid number for a bet")
        else:
            if chips.bet > chips.total:
                print("Not enough chips, you only have {}".format(chips.total))
            else:
                bet_required = False

# Draw card of the deck
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

# Process player action
def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input('Hit or Stand (h or s): ').lower()
        if x == 'h':
            hit(deck,hand)
        elif x == 's':
            print("Player stands")
            playing = False
        else:
            print("Choose h or s")
            continue
        break

# show one of the dealer's cards
def show_some(player,dealer):

    print("\nDealer's hand is: ")
    print("First card is hidden")
    print(dealer.cards[-1])
    
    #Show the player cards
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)
          
def show_all(player,dealer):
    #print dealer cards
    print("\nDealer's hand:")
    for card in dealer.cards:
        print(card)
    #Calculate value of cards in hand
    print(f"Value of Dealer: {dealer.value}")
    
    #Same for player
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player: {player.value}")

# Process hand results
def player_busts(player,dealer,chips):
    print("Player bust")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.lose_bet()
    
def push(player,dealer):
    print("Push!")


# Set up the Player's chips
player_chips = Chips()   

# Print an opening statement
print("Welcome to the game")
print("You start with 100 Chips")

# Main game loop
while True:  
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    

    
    # Prompt the Player for their bet
    take_bet(player_chips)
  
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total 
    print("\nPlayer total chips are at: {}".format(player_chips.total))
    # Ask to play again
    new_game = input("Would you like to play another hand (Y or N)?").lower()
    
    if new_game == 'y':
        playing =  True
        continue
    else:
        print("Thank you for playing")
        break