# Build Container
docker-compose build

# Run Container
docker run --name event-solr -d -p 8983:8983 -t event-solr

# Start/Stop Container
docker start event-solr
docker stop event-solr

# Remote
docker rm event-solr
docker rmi event-solr
