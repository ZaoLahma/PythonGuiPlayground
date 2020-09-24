from core.log.log import Log
from gui.window import Window
from gui.workspace.ws_start import WsStart
from gui.workspace.ws_test import WsTest

class Main:
    @staticmethod
    def run():
        Log.log_application_name = "Test"
        Log.log("Starting...")
        window = Window()
        window.add_workspace(WsStart)
        window.add_workspace(WsTest)
        window.activate_workspace(WsStart)

        window.run()


if "__main__" == __name__:
    Main.run()
        