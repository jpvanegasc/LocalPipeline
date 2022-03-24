default: ingest extract

docker:
	docker-compose up -d

ingest:
	docker exec local_pipeline python src/extract.py $(year) $(month)

extract:
	docker exec local_pipeline python src/load.py $(year) $(month)