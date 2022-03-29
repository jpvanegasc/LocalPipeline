default: ingest extract quality

docker:
	docker-compose up -d

ingest:
	docker exec local_pipeline python src/extract.py $(year) $(month)

extract:
	docker exec local_pipeline python src/load.py $(year) $(month)

quality:
	docker exec local_pipeline python src/quality.py
