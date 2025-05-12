#!/bin/bash

COLD_START=false
if [[ "$1" == "--cold-start" ]]; then
  COLD_START=true
  echo "🧹 Cold start enabled: Removing previous containers and volumes..."
  docker-compose down -v
fi

START=$(date +%s)
echo "⏳ Starting containers..."
docker-compose up -d

echo -e "\\n📦 Image sizes:"
docker images | grep -E 'elasticsearch|kibana'

echo -e "\\n🔍 Waiting for Elasticsearch to start..."
until docker logs elasticsearch 2>&1 | grep -q "started"; do
  sleep 2
done
echo "✅ Elasticsearch started."

echo -e "\\n📊 Waiting for Kibana to be ready..."
until docker logs kibana 2>&1 | grep -q "Kibana is now available" || docker logs kibana 2>&1 | grep -q "Server running at http"; do
  sleep 2
done
echo "✅ Kibana is ready."

END=$(date +%s)
echo -e "\\n⏱️ Total startup time: $((END - START)) seconds"