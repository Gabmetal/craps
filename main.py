import curses
import random
CFG_INITMONEY = 1000

class Player():
    wallet = 0

class Game():
    screen = curses.initscr()
    i = 0
    p = Player()
    roll = 0
    point = 0
    dado1 = 0
    dado2 = 0
    passline = 0
    nopassline = 0
    field = 0
    hardway = 0

    def start(self):
        self.p.wallet = CFG_INITMONEY
        self.screen.border(0)
        self.screen.refresh()
        self.loop()

    def base_screen(self):
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(2, 2, "PyCraps Game 0.1 Alpha - Gabriel Cavallo")
        self.screen.addstr(2, 100, "Billetera $")
        self.screen.addstr(2, 112, str(self.p.wallet))
        self.screen.addstr(4, 100, "Dado 1:")
        self.screen.addstr(4, 108, str(self.dado1))
        self.screen.addstr(5, 100, "Dado 2:")
        self.screen.addstr(5, 108, str(self.dado2))
        self.screen.addstr(6, 100, "Tiro: ")
        self.screen.addstr(6, 108, str(int(self.dado1 + self.dado2)))
        self.screen.addstr(7, 100, "Punto:")
        self.screen.addstr(7, 108, str(self.point))
        self.screen.addstr(9, 101, "*Apuestas*")
        self.screen.addstr(11, 100, "Passline      $")
        self.screen.addstr(11, 117, str(self.passline))
        self.screen.addstr(12, 100, "Don'tPassline $")
        self.screen.addstr(12, 117, str(self.nopassline))
        self.screen.addstr(13, 100, "Field         $")
        self.screen.addstr(13, 117, str(self.field))
        self.screen.addstr(14, 100, "HardWay       $")
        self.screen.addstr(14, 117, str(self.hardway))

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
        self.screen.refresh()
        self.p.wallet -= int(float(betinput))
        self.screen.addstr(4, 4, "En que modalidad quiere apostar?")
        self.screen.addstr(5, 4, "1 - Passline")
        self.screen.addstr(6, 4, "2 - Don't Passline")
        self.screen.addstr(7, 4, "3 - Field")
        self.screen.addstr(8, 4, "4 - HardWay")
        self.screen.addstr(9, 4, "5 - Atras")

        x = self.screen.getch()

        if x == ord('1'):
            self.passline += int(float(betinput))
        elif x == ord('2'):
            self.nopassline += int(float(betinput))
        elif x == ord('3'):
            self.field += int(float(betinput))
        elif x == ord('4'):
            self.hardway += int(float(betinput))
        elif x == ord('5'):
            self.main_menu()
        else:
            self.bet_menu()

        self.screen.refresh()
        self.dice()

    def rule(self):
        if point == 0:
            if roll == 7 or roll == 11:
                self.p.wallet += self.passline*2
                self.passline = 0
                self.nopassline = 0
                self.p.wallet += self.field*2
            elif roll == 2 or roll == 3 or roll == 12:
                self.passline = 0
                self.p.wallet += self.nopassline*2
                if roll == 2 or roll == 12:
                    self.p.wallet += self.field*3
                    self.p.wallet += self.hardway*8
                elif roll == 3:
                    self.p.wallet += self.field*2
                    self.p.wallet += self.hardway*10
            else:
                if roll == 4:
                    self.p.wallet += self.field*2
                    self.p.wallet += self.hardway*8
                elif roll == 5:
                    self.field = 0
                    self.p.wallet += self.hardway*8
                elif roll== 6 or roll == 8:
                    self.field = 0
                    self.p.wallet += self.hardway*10
                elif roll == 9:
                    self.p.wallet += self.field*2
                    self.hardway = 0
                elif roll == 10:
                    self.p.wallet += self.field*2
                    self.p.wallet += self.hardway*8
        self.main_menu()


    def dice(self):
        self.dado1, self.dado2 = random.randint(1,6), random.randint(1,6)
        self.base_screen()
        self.screen.refresh()
        self.roll = self.dado1 + self.dado2
        if self.point == 0:
            self.point = self.roll
        self.main_menu()

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
