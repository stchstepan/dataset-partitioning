import re

class FileAccessPermissions:
    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path

    def has_setuid_setgid(self):
        with open(self.dockerfile_path, 'r') as file:
            dockerfile_content = file.read()

        setuid_setgid_pattern = r'chmod .*(u\+s|g\+s|\d{4}([0-7]1[0-7]))'

        matches = re.findall(setuid_setgid_pattern, dockerfile_content)
        if matches:
            return True
        else:
            return False