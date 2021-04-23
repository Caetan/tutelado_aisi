###################  Docker development directives  ####################
#
# Usage:
# make env              # build environment, create and start containers
# make build			# force rebuild image and environment
# make stop				# stops containers
# make clean			# removes container, network and volume

env:
	docker-compose up --force-recreate --remove-orphans
.PHONY: env

build:
	docker-compose build --force-rm
	make env
.PHONY: stop

stop:
	docker-compose stop
.PHONY: stop

clean:
	docker-compose down -v
.PHONY: clean
