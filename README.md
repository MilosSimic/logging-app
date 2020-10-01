[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)

# logging-app
Simple test app that logs user activity from Django app to ELK stack using Docker.

# Steps
- Delete pgadata
- Remove esdata, influx folder content
- Watch loags for postress and elasticsearch!

# Dashboard access
- Kibana dashboard: http://localhost:5601
- Influx dashboard: http://localhost:8083 (vm_metrics, docker_metrics) (show measurements)
- Grafana dashboard: http://localhost:3000 (admin, admin)
- App: http://localhost:8000 [/about, /test, /list_all/] **list_all serve static files over nginx**

# Grafana notes
- For Grafana to show results, choose _Datasource_ add some (vm_metrics, docker_metrics) or both if you want to use more than one source. 
- For _type_ choose _influx_ with url http://influxdb:8086 (this is docker compose name and port)
- For _access_ choose _proxy_
- For database data choose _vm_metrics_ **or** _docker_metrics_ these are influx names

# Show graph
- Goto _New Dashboard_ > _Graph_ 
- Click on _Panel Title_ and choose _edit_ 
- From _default_ choose_value to watch for
- Than from Select statement choose filed

# Gunicorn
Check [gunicorn](https://github.com/MilosSimic/logging-app/blob/master/start.sh) setup

## Travis tutorial
- Tutorial for travis CICD can be found [here](https://github.com/MilosSimic/Travis-tutorial)
- Docker image for Travis CLI can be found [here](https://github.com/MilosSimic/mytravis)

# More materials
- Grafana create dashboard InfluxDB data [video](https://www.youtube.com/watch?v=FBAKSgWgOz8)
- Influxdb and grafana by docker [page](https://blog.laputa.io/try-influxdb-and-grafana-by-docker-6b4d50c6a446)
