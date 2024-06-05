# README.md

## Project Overview

This project consists of two main modules, each designed to evaluate the security of different types of files: Dockerfiles and Kubernetes deployments. The modules analyze various attributes of these files to determine their security levels based on predefined criteria.

## Directory Structure

The project's directory structure is organized as follows:

```
Deployments/
  ├── attributes/
  │   ├── ExposePortKubernetes.py
  │   ├── KubernetesCapabilities.py
  │   ├── KubernetesDeploymentDangerousCommandsChecker.py
  │   ├── KubernetesDeploymentLatestTagChecker.py
  │   ├── KubernetesEmptyDirMount.py
  │   ├── KubernetesHostSeparation.py
  │   ├── KubernetesNonRootUser.py
  │   ├── KubernetesProbeChecker.py
  │   ├── KubernetesReadOnlyRootFS.py
  │   ├── KubernetesResourceChecker.py
  │   ├── KubernetesSecrets.py
  │   ├── KubernetesVolumePermissions.py
  │   ├── PrivilegedSecurityContextKubernetes.py
  │   └── SecretEnvironmentVariablesKubernetes.py
  └── main.py

Dockerfiles/
  ├── attributes/
  │   ├── EndOfInstallationCleaning.py
  │   ├── ExposedPorts.py
  │   ├── FileAccessPermissions.py
  │   ├── NonLatestImageUsagePolicy.py
  │   ├── NonRootUser.py
  │   ├── OfficialBaseImage.py
  │   ├── PackageUpdates.py
  │   ├── SafeCommands.py
  │   └── SafeCopy.py
  └── main.py
```

## Dockerfiles Module

The Dockerfiles module evaluates the security of Dockerfiles based on multiple attributes. The script can be executed from the `Dockerfiles` directory.

### Attributes

1. **NonRootUser**: Checks if the Dockerfile uses a non-root user.
2. **FileAccessPermissions**: Checks for the presence of setuid and setgid.
3. **SafeCommands**: Identifies potentially dangerous commands.
4. **OfficialBaseImage**: Verifies if an official base image is used.
5. **NonLatestImageUsagePolicy**: Ensures the image is not using the latest tag.
6. **PackageUpdates**: Checks for package update commands.
7. **SafeCopy**: Ensures safe file copying practices.
8. **EndOfInstallationCleaning**: Validates the presence of cleanup commands after installation.
9. **ExposePort**: Checks for exposed ports.

### Running the Script

Navigate to the `Dockerfiles` directory and execute the `main.py` script:

```bash
cd Dockerfiles
python main.py
```

The script analyzes Dockerfiles in the specified directory and prints the security status of each file.

### Dataset

The dataset for Dockerfiles can be found on [Kaggle](https://www.kaggle.com/datasets/stanfordcompute/dockerfiles/).

## Kubernetes Deployments Module

The Kubernetes Deployments module evaluates the security of Kubernetes deployment YAML files. The script can be executed from the `Deployments` directory.

### Attributes

1. **KubernetesHostSeparation**: Checks for proper host separation.
2. **PrivilegedSecurityContextKubernetes**: Ensures the deployment does not use privileged security contexts.
3. **KubernetesCapabilities**: Checks for dangerous capabilities.
4. **KubernetesNonRootUser**: Verifies the deployment runs as a non-root user.
5. **KubernetesSecrets**: Ensures secrets are managed securely.
6. **SecretEnvironmentVariablesKubernetes**: Checks for the usage of secret environment variables.
7. **KubernetesReadOnlyRootFS**: Validates the root filesystem is read-only.
8. **KubernetesDeploymentDangerousCommandsChecker**: Identifies dangerous commands.
9. **KubernetesEmptyDirMount**: Ensures emptyDir mounts are secure.
10. **ExposePortKubernetes**: Checks for exposed ports.
11. **KubernetesDeploymentLatestTagChecker**: Ensures the deployment does not use the latest tag.
12. **KubernetesVolumePermissions**: Verifies volume permissions.
13. **KubernetesResourceChecker**: Checks resource requests and limits.
14. **KubernetesProbeChecker**: Ensures probes are configured.

### Running the Script

Navigate to the `Deployments` directory and execute the `main.py` script:

```bash
cd Deployments
python main.py
```

The script analyzes Kubernetes deployment YAML files and prints the security status of each deployment.
