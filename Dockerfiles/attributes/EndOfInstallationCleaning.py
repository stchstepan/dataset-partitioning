class EndOfInstallationCleaning:
    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path

    def has_package_installation(self):
        with open(self.dockerfile_path, 'r') as file:
            dockerfile_content = file.readlines()

        package_managers = ["apt-get", "yum", "apk"]

        for line in dockerfile_content:
            if line.strip().startswith("#"):
                continue
            
            for manager in package_managers:
                if manager in line and ("install" in line or "add" in line):
                    return True

        return False

    def has_required_instructions(self):
        if not self.has_package_installation():
            return True

        with open(self.dockerfile_path, 'r') as file:
            dockerfile_content = file.readlines()

        required_commands = [
            "--no-install-recommends",
            "rm -rf /var/lib/apt/lists/*",
            "yum clean all",
            "apt-get clean",
            "apk del .build-deps"
        ]

        found_commands = set()

        for line in dockerfile_content:
            if line.strip().startswith("#"):
                continue
            
            for cmd in required_commands:
                if cmd in line:
                    found_commands.add(cmd)

        return len(found_commands) >= 2