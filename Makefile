DC = docker-compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
FRONTEND_FILE = docker-compose/frontend.yml
BACKEND_FILE = docker-compose/backend.yml
STORAGES_FILE = docker-compose/storages.yml
BACKEND_APP_CONTAINER = backend-app
FRONTEND_APP_CONTAINER = frontend-app


# ------------------------------------------

.PHONY: all
all:
	${DC} -f ${STORAGES_FILE} -f ${BACKEND_FILE} -f ${FRONTEND_FILE} ${ENV} up --build -d

.PHONY: all-down
all-down:
	${DC} -f ${STORAGES_FILE} -f ${BACKEND_FILE} -f ${FRONTEND_FILE} ${ENV} down

# ------------------------------------------

.PHONY: frontend
frontend:
	${DC} -f ${FRONTEND_FILE} ${ENV} up --build -d

.PHONY: frontend-down
frontend-down:
	${DC} -f ${FRONTEND_FILE} down

.PHONY: frontend-logs
frontend-logs:
	${LOGS} ${FRONTEND_APP_CONTAINER} -f

# ------------------------------------------

.PHONY: backend
backend:
	${DC} -f ${BACKEND_FILE} ${ENV} up --build -d

.PHONY: backend-down
backend-down:
	${DC} -f ${BACKEND_FILE} down

.PHONY: backend-logs
backend-logs:
	${LOGS} ${BACKEND_APP_CONTAINER} -f

.PHONY: backend-shell
backend-shell:
	${EXEC} ${BACKEND_APP_CONTAINER} bash

.PHONY: backend-makemigrations
backend-makemigrations:
	${EXEC} ${BACKEND_APP_CONTAINER} alembic revision --autogenerate
# ------------------------------------------

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

# ------------------------------------------