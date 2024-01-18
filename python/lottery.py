import string
from random import randint, choice

TICKETS = [
    '5678B', '9876C', '2345D', '6789E', '3456F', '8765G', '4321H', '7890J', '5432K', '2109L',
    '1357N', '2468P', '6543Q', '7891R', '3579S', '9821T', '4682U', '5763V', '1234A', '8765M', 
]
TICKET_COST = 1
BILLS_ACCEPTED = [1, 5]


class Lottery:
    available_tickets = TICKETS.copy()
    chosen_tickets = []

    def __user_input(self):
        pass

    def __payment(self):
        pass

    def __generate_winner_ticket(self):
        ticket = ''

        for _ in range(4):
            ticket += str(randint(0, 9))
        ticket += choice(string.ascii_uppercase)

        self.__winner_ticket = ticket

    def __check_win(self):
        pass

    def main(self):
        # Flow: user choose quantity of tickets and tickets from the TICKETS list
        # Then, system prompt the user to pay in cash or by bank card, return the change if applicable
        # Ticket is issued after payment, The user returns to the main menu to play the lottery
        # The lottery system generates 1 random ticket code
        self.__generate_winner_ticket()
        print(self.__winner_ticket)


def run():
    lottery = Lottery()
    lottery.main()


if __name__ == '__main__':
    run()
