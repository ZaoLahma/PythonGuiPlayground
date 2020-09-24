from .workspace_base import WorkspaceBase
from core.log.log import Log
from tkinter import ttk

class WsTest(WorkspaceBase):
    def __init__(self, parent_frame, ws_controller):
        Log.log("WsTest init called")
        WorkspaceBase.__init__(self, parent_frame, ws_controller)
        ws_header = ttk.Label(self, text = "This is the test workspace")
        ws_header.grid(row = 0, column = 0)

    @staticmethod
    def get_id():
        return "Test"

    def activate(self):
        Log.log("Activate called")

    def pause(self):
        Log.log("Pause called")

    def destroy(self):
        Log.log("Destroy called")