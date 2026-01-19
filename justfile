set shell := ["powershell.exe", "-c"]

RESEARCH_PROMPT := "Can you design a really unique python library in a single code snippet."

default:
	just --list

docker-build-run:
	docker build -t million-monkeys .
	docker run --rm -it million-monkeys

install-packages:
	uv pip install -r pyproject.toml

run-celery-test +user_request:
	python run_celery_workflow.py {{user_request}}

run-celery-test-research:
	python run_celery_workflow.py {{RESEARCH_PROMPT}}

run-test +user_request:
	python run_workflow.py {{user_request}}

run-test-research:
	python run_workflow.py {{RESEARCH_PROMPT}}