import docker

def stream():
  client = docker.DockerClient(base_url='unix://var/run/docker.sock')
  stream = client.events(decode=True)
  selfhost = client.info()['Name']

  return stream, selfhost


