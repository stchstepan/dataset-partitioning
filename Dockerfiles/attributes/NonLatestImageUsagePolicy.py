class NonLatestImageUsagePolicy:
    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path

    def is_latest_version(self):
        with open(self.dockerfile_path, 'r') as file:
            dockerfile_content = file.read()

        from_line = next((line for line in dockerfile_content.split('\n') if line.startswith('FROM ')), None)

        if from_line:
            image_name_with_version = from_line.split(' ')[1]
            if ':' in image_name_with_version:
                _, version = image_name_with_version.split(':', 1)
                return version.strip() == 'latest'
            else:
                return False
        else:
            return False
