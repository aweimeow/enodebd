# ONF enodebd Makefile
#
# SPDX-FileCopyrightText: © 2020 Open Networking Foundation <support@opennetworking.org>
# SPDX-License-Identifier: Apache-2.0

# Use bash for pushd/popd, and to fail quickly.
# No -u as virtualenv activate script has undefined vars
SHELL = bash -e -o pipefail

# tooling
VIRTUALENV        ?= python3 -m venv

# all files with extensions
PYTHON_FILES      ?= $(wildcard devices/freedomfi_one.py devices/device_utils.py devices/device_map.py)

.DEFAULT_GOAL := help
.PHONY: test lint license help

# Create the virtualenv with all the tools installed
VENV_NAME = venv

$(VENV_NAME): requirements.txt
	$(VIRTUALENV) $@ ;\
  source ./$@/bin/activate ; set -u ;\
  python -m pip install --upgrade pip;\
  python -m pip install -r requirements.txt
	echo "To enter virtualenv, run 'source $@/bin/activate'"

install-protoc: ## Get the protobyf from GitHub
	curl -L https://github.com/protocolbuffers/protobuf/releases/download/v3.19.4/protoc-3.19.4-linux-x86_64.zip -o /opt/protoc.zip ;\
  unzip -o /opt/protoc.zip -d /opt/protobuf ;\
  ln -sf /opt/protobuf/bin/protoc /usr/bin/

proto: $(VENV_NAME) ## Compile proto definition of enodebd
	source ./$</bin/activate ; set -u ;\
  python tools/gen_protos.py proto_files/orc8r/protos \
     proto_files,proto_files/orc8r/protos/prometheus,/opt/protobuf/include proto_files . ;\
  python tools/gen_protos.py proto_files/lte/protos \
     proto_files,proto_files/orc8r/protos/prometheus,/opt/protobuf/include proto_files . ;\
  python tools/gen_prometheus_proto.py . .

license: $(VENV_NAME) ## Check license with the reuse tool
	source ./$</bin/activate ; set -u ;\
  reuse --version ;\
  reuse --root . lint

test: flake8 pylint black ## run all standard tests

flake8: $(VENV_NAME) ## check python formatting with flake8
	source ./$</bin/activate ; set -u ;\
  flake8 --version ;\
  flake8 --max-line-length 99 --per-file-ignores="__init__.py:F401" $(PYTHON_FILES)

pylint: $(VENV_NAME) ## pylint check for python 3 compliance
	source ./$</bin/activate ; set -u ;\
  pylint --version ;\
  pylint --rcfile=pylint.ini $(PYTHON_FILES)

black: $(VENV_NAME) ## run black on python files in check mode
	source ./$</bin/activate ; set -u ;\
  black --version ;\
  black --check $(PYTHON_FILES)

blacken: $(VENV_NAME) ## run black on python files to reformat
	source ./$</bin/activate ; set -u ;\
  black --version ;\
  black $(PYTHON_FILES)

clean:
	rm -rf $(VENV_NAME) ansible_collections

help: ## Print help for each target
	@echo enodebd make targets
	@echo
	@grep '^[[:alnum:]_-]*:.* ##' $(MAKEFILE_LIST) \
    | sort | awk 'BEGIN {FS=":.* ## "}; {printf "%-25s %s\n", $$1, $$2};'
