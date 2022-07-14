### --------------------------------------------------------------------------------------------------------------------
### Variables
### (https://www.gnu.org/software/make/manual/html_node/Using-Variables.html#Using-Variables)
### --------------------------------------------------------------------------------------------------------------------

CONTAINER_NAME = diagrams
CONTAINER_ID_ENV = DAC_CONTAINER_ID
IMAGE_NAME := $(CONTAINER_NAME)

JAVA_JARS_LOCATION := /jars
PY_DAC_CONTAINER_LOCATION := /diagrams/py
UML_DAC_CONTAINER_LOCATION := /diagrams/uml

OUTPUT_HOST_LOCATION := ${PWD}/output
OUTPUT_HOST_LOCATION_PY := ${OUTPUT_HOST_LOCATION}/py
OUTPUT_HOST_LOCATION_UML := ${OUTPUT_HOST_LOCATION}/uml

# Other config
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m


### --------------------------------------------------------------------------------------------------------------------
### RULES
### (https://www.gnu.org/software/make/manual/html_node/Rule-Introduction.html#Rule-Introduction)
### --------------------------------------------------------------------------------------------------------------------
.PHONY: generate-py generate-puml

help:
	@echo 	"Please use \`make <target>' where <target> is one of"
	@echo	"  generate-py      generate DaC image using the python diagrams pacakage"
	@echo	"  generate-puml    generate DaC image using PlantUML and C4"

setup:
	docker build -t $(CONTAINER_NAME) .

clean: stop-container

create-host-outputs:
	mkdir -p $(OUTPUT_HOST_LOCATION)
	mkdir -p $(OUTPUT_HOST_LOCATION)/py
	mkdir -p $(OUTPUT_HOST_LOCATION)/uml

run-container: create-host-outputs setup
	docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop-container:
	docker rm -f ${DAC_CONTAINER_ID}

generate-py:
	@printf "$(OK_COLOR)==> Running DaC Python $(NO_COLOR)\n"
	docker exec -t $(CONTAINER_NAME) sh -c "cd $(PY_DAC_CONTAINER_LOCATION); python3 $(filename).$(inputext); ls -lah"

copy-file-py:
	@printf "$(OK_COLOR)==> Copying file to Host location $(OUTPUT_HOST_LOCATION) $(NO_COLOR)\n"
	docker cp $(CONTAINER_NAME):$(PY_DAC_CONTAINER_LOCATION)/$(filename).$(outputext) $(OUTPUT_HOST_LOCATION_PY)

generate-uml:
	@printf "$(OK_COLOR)==> Running DaC UML $(NO_COLOR)\n"
	docker exec -t $(CONTAINER_NAME) sh -c "cd $(UML_DAC_CONTAINER_LOCATION); echo $(pwd); java -jar $(JAVA_JARS_LOCATION)/plantuml.jar $(filename).$(inputext); ls -lah"

copy-file-uml:
	@printf "$(OK_COLOR)==> Copying file to Host location $(OUTPUT_HOST_LOCATION) $(NO_COLOR)\n"
	docker cp $(CONTAINER_NAME):$(UML_DAC_CONTAINER_LOCATION)/$(filename).$(outputext) $(OUTPUT_HOST_LOCATION_UML)

diagrams-py: generate-py copy-file-py

diagrams-uml: generate-uml copy-file-uml
