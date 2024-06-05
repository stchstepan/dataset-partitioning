import re

class SafeCommands:
    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path

    def has_potentially_dangerous_commands(self):
        with open(self.dockerfile_path, 'r') as file:
            dockerfile_content = file.read()

        dangerous_commands = [
            "wget ",
            "curl ",
            "git clone ",
            "add-apt-repository ",
            "ppa:",
            "ssh",
            "&& wget ",
            "&& curl ",
            "&& git clone ",
        ]

        for cmd in dangerous_commands:
            if re.search(re.escape(cmd), dockerfile_content):
                return True

        return False
