class ExposePortKubernetes:
    def __init__(self, deployment_content):
        self.deployment_content = deployment_content

    def has_exposed_ports(self):
        ports_found = False

        for line in self.deployment_content.split('\n'):
            if "ports:" in line:
                ports_found = True
                break

        return ports_found

    def _is_valid_unix_port(self, port):
        try:
            port_number = int(port)
            if port_number >= 0 and port_number <= 65535:
                return True
            else:
                return False
        except ValueError:
            return False