import yaml

class KubernetesResourceChecker:
    def __init__(self, deployment_content):
        self.deployment_content = deployment_content

    def check_resources(self):
        deployment_content_dict = yaml.safe_load(self.deployment_content)

        containers = deployment_content_dict.get('spec', {}).get('template', {}).get('spec', {}).get('containers', [])
        for container in containers:
            resources = container.get('resources', {})
            if 'requests' in resources or 'limits' in resources:
                return True
        return False
