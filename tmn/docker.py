import docker as dockerpy


class DockerManager:
    """
    Manage interactions with the docker daemon.
    """

    def __init__(self):
        self.client = dockerpy.from_env()

    def ping(self):
        """
        Try to ping the Docker deamon to see if it's accessible.

        :returns: Is Docker running
        :rtype: bool
        """
        try:
            return self.client.ping()
        except Exception as e:
            return False