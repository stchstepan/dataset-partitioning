class ExposePort:
    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path

    def has_exposed_ports(self):
        with open(self.dockerfile_path, 'r') as file:
            dockerfile_content = file.readlines()

        expose_found = False

        for line in dockerfile_content:
            if line.strip().startswith("#"):
                continue

            if line.strip().startswith("EXPOSE"):
                expose_found = True
                ports = line.strip().split()[1:]
                if ports:
                    for port in ports:
                        if not self._is_valid_unix_port(port):
                            return False
                    return True

        if expose_found:
            return False

        return False

    def _is_valid_unix_port(self, port):
        try:
            port_number = int(port)
            if port_number >= 0 and port_number <= 65535:
                return True
            else:
                return False
        except ValueError:
            return False