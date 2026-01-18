set shell := ["powershell.exe", "-c"]

default:
	just --list

docker-build-run:
	docker build -t million-monkeys .
	docker run --rm -it million-monkeys

@run-test user_request:
	python run_workflow.py $user_request
