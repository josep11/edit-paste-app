default: help

include .make/*.mk

## Tail the logs
logs-tail:
	@sh ./tail-logs.sh

## Tail the logs
tail-logs: logs-tail

## Build
build:
	$(shell ./build.zsh)

## Build and run
build-and-run:
	@echo ./build_and_run.zsh
# $(shell ./build_and_run.zsh)

## Build and deploy
build-and-deploy:
	@echo ./build_and_deploy.zsh

## Cleans up already merged branches
git/clean:
	git fetch origin --prune

## Ensures that the the requirements for dev are installed
_ensure-requirements-dev:
	@pytest --version >/dev/null 2>&1 || (echo "ERROR: pytest is required. Please run make pip/install-dev"; exit 1)

## Run unit tests
test:
	make _ensure-requirements-dev
	pytest -q