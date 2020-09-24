from core.log.log import Log

class WorkspaceController:
    def __init__(self):
        Log.log("WorkspaceController init")
        self.workspaces = {}

    def add_workspace(self, workspace):
        self.workspaces[workspace.get_id()] = workspace

    def activate_workspace(self, WS_CLASS):
        workspace = self.workspaces[WS_CLASS.get_id()]
        workspace.activate()
        workspace.tkraise()
        Log.log("Activated workspace " + workspace.get_id())

    def get_workspaces(self):
        return self.workspaces