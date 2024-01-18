# Docker Event Monitor (Reforged: Sentry integration) originally from [DEM](https://bitbucket.org/quaideman/dem/src/master/app/).

### What is it?
A tiny container that monitors the local Docker event system in real-time and sends out notifications to various integrations for event types that match the configuration.

For example, you can trigger an alert when a container is stopped, killed, runs out of memory or health status change.

For a full list of events that are supported see the official [Docker Documentation](https://docs.docker.com/engine/reference/commandline/events/).

### Features
- Integrations for **Sentry**.
- Customisable event triggers.

### Quick Start
Build your own image and run the container on the host you want to monitor mounting in the `docker.sock`:

```
docker build -t monitor:latest .
```

```
docker run --rm \
-v /var/run/docker.sock:/var/run/docker.sock \
monitor:latest
```
### Configuration
Example `conf.yml` with a subset of available event types that will trigger a notification. For a full list of all available event types please see the official [Docker Documentation](https://docs.docker.com/engine/reference/commandline/events/).

```
events:
  container: 
    - die
    - oom
    - destroy
    - create
  image: 
    - delete
  plugin:
    - install
    - remove
  volume: 
    - destroy
    - create
  network:
    - destroy
  daemon:
    - reload
  service:
    - remove
  node:
    - remove
  secret:
    - remove
  config:
    - remove

```

### Integrations
#### Sentry
To configure Monitor to work with Sentry you will need to define a Sentry DSN in .env file (see .env.example).  Please see the official [Sentry documentation](https://docs.sentry.io/platforms/python/).

