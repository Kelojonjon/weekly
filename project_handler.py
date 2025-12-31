from pathlib import Path
import json

class PROJECT_HANDLER():

    def __init__(self):
        self.script_path = Path(__file__).resolve()
        self.script_dir = self.script_path.parent
        
        # Create project_dir if none exists
        (self.script_dir / "projects").mkdir(exist_ok=True)
        self.project_dir = self.script_dir / "projects"        

        # Json file paths
        self.state_path = self.project_dir / "state.json"

        # Load json files to ram
        self.state = None

        #State template
        self.template = {
                "week_id": None,
                "score": 0,
                "streak": 0,
                "topic": "No topics loaded, use 'add topic:topic:topic' to add topics!",
                "completed": False,
                "rotation": [],
                "done_topics": [],
                }
  
    def is_project(self):
        project_exists = self.state_path.exists()
        if not project_exists:
            (self.project_dir / "state.json").touch(exist_ok=True)
            template = json.dumps(self.template, indent=2)
            self.state_path.write_text(template)

    def reset(self):
        (self.project_dir / "state.json").touch()
        template = json.dumps(self.template, indent=2)
        self.state_path.write_text(template)

    def init(self):
        self.is_project()
        self.load_project()

    def load_json(self, path):
        with open(path, "r") as f:
            read_json = json.load(f)
            return read_json

    def save_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
    
    def load_project(self):
        self.state = self.load_json(self.state_path)

    def save_project(self):
            self.save_json(self.state_path, self.state)




