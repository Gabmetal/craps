import curses

CFG_INITMONEY = 1000

class Player():
    wallet = 0

class Game():
    screen = curses.initscr()
    i = 0
    p = Player()

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
        self.screen.addstr(4, 100, str(self.p.wallet))

    def add_wallet(self):
        self.base_screen()
        self.screen.addstr(4, 4, "Ingrese la Cantidad en Dinero Que Quiere Agregar")
        self.screen.refresh()
        walletinput = self.screen.getstr(6, 4, 60)
        self.p.wallet += int(float(walletinput))
        self.main_menu()

    def main_menu(self):
        self.base_screen()
        self.screen.addstr(4, 4, "1 - Agregar Dinero")
        self.screen.addstr(7, 4, "9 - Salir")
        self.screen.refresh()
        x = self.screen.getch()

        if x == ord('1'):
            self.add_wallet()
        if x == ord('9'):
            curses.endwin()


    def loop(self):
        self.main_menu()
        curses.endwin()

app = Game()
app.start()
