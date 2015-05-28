import curses
import random
CFG_INITMONEY = 1000

class Player():
    wallet = 0

class Game():
    screen = curses.initscr()
    i = 0
    p = Player()
    point = 0
    dado1 = 0
    dado2 = 0

    def start(self):
        self.p.wallet = CFG_INITMONEY
        self.screen.border(0)
        self.screen.refresh()
        self.loop()

    def base_screen(self):
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(2, 2, "PyCraps Game 0.1 Alpha - Gabriel Cavallo")
        self.screen.addstr(2, 100, "Billetera")
        self.screen.addstr(2, 110, str(self.p.wallet))
        self.screen.addstr(4, 100, "Dado 1:")
        self.screen.addstr(4, 108, str(self.dado1))
        self.screen.addstr(5, 100, "Dado 2:")
        self.screen.addstr(5, 108, str(self.dado2))
        self.screen.addstr(7, 100, "Punto:")
        self.screen.addstr(7, 108, str(self.point))


    def add_wallet(self):
        self.base_screen()
        self.screen.addstr(4, 4, "Ingrese la Cantidad en Dinero Que Quiere Agregar")
        self.screen.refresh()
        walletinput = self.screen.getstr(6, 4, 60)
        self.p.wallet += int(float(walletinput))
        self.main_menu()

    def add_bet(self):
        self.base_screen()
        self.screen.addstr(4, 4, "Ingrese la Cantidad en Dinero Que Quiere Apostar")
        self.screen.refresh()
        betinput = self.screen.getstr(6, 4, 60)
        self.p.wallet -= int(float(betinput))

    def bet_menu(self):
        self.base_screen()
        self.screen.addstr(4, 4, "1 - Passline")
        self.screen.addstr(5, 4, "2 - Don't Passline")
        self.screen.addstr(6, 4, "3 - Field")
        self.screen.addstr(7, 4, "4 - HardWay")
        self.screen.addstr(8, 4, "5 - Atras")
        self.screen.refresh()
        x = self.screen.getch()


    def dice(self):
        self.dado1, self.dado2 = random.randint(1,6), random.randint(1,6)
        self.base_screen()
        self.screen.refresh()
        roll = self.dado1 + self.dado2
        if self.point == 0:
            self.point = roll

    def main_menu(self):
        self.base_screen()
        self.screen.addstr(4, 4, "1 - Agregar Dinero")
        self.screen.addstr(5, 4, "2 - Realizar apuesta")
        self.screen.addstr(6, 4, "3 - Tirar dados")
        self.screen.addstr(7, 4, "9 - Salir")
        self.screen.refresh()
        x = self.screen.getch()

        if x == ord('1'):
            self.add_wallet()
        elif x == ord('2'):
            self.add_bet()
        elif x == ord('3'):
            self.dice()
        elif x == ord('9'):
            curses.endwin()
        else:
            self.main_menu()


    def loop(self):
        self.main_menu()
        curses.endwin()

app = Game()
app.start()
