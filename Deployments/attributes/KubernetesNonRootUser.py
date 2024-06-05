class KubernetesNonRootUser:
    def __init__(self, deployment_content):
        self.deployment_content = deployment_content

    def check_non_root_execution(self):
        non_root_exec_indicators = ["user: root", "runAsUser: 0"]

        for line in self.deployment_content.split('\n'):
            if any(indicator in line for indicator in non_root_exec_indicators):
                return False

        return True