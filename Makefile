.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%s%-35s%s %s\n", "${CYAN}", $$1, "${DEFAULT}",$$2}'

.PHONY: start
start: ## Start the Jupyter Notebook container.
	docker-compose build && docker-compose up

.PHONY: stop
stop: ## Stop the Jupyter Notebook container.
	docker-compose stop && docker-compose down
