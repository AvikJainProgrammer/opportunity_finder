# Makefile for setting up a Python virtual environment and installing dependencies on Windows

# Define the name of the virtual environment
VENV_NAME = venv

# Define the Python interpreter (you can specify python3 if needed)
PYTHON = python

# Default target
all: venv install

# Create a virtual environment
venv:	
	@echo Creating virtual environment...
	$(PYTHON) -m venv $(VENV_NAME)
	@echo Virtual environment created at $(VENV_NAME)/

# Install dependencies from requirements.txt
install: venv
	@echo Installing dependencies...
	$(VENV_NAME)\Scripts\activate.bat && pip install -r requirements.txt


# Configure VS Code settings
configure_vscode:
	@echo Configuring VS Code settings...
	@mkdir .vscode 2> NUL || echo .vscode folder already exists
	@echo { > .vscode/settings.json
	@echo   "python.defaultInterpreterPath": "${workspaceFolder}/$(VENV_NAME)/Scripts/python.exe", >> .vscode/settings.json
	@echo   "python.venvPath": "${workspaceFolder}/$(VENV_NAME)", >> .vscode/settings.json
	@echo   "python.linting.enabled": true, >> .vscode/settings.json
	@echo   "python.linting.pylintEnabled": true, >> .vscode/settings.json
	@echo   "editor.formatOnSave": true, >> .vscode/settings.json
	@echo   "python.testing.pytestEnabled": true, >> .vscode/settings.json
	@echo   "python.testing.pytestArgs": ["tests"] >> .vscode/settings.json
	@echo } >> .vscode/settings.json
	@echo VS Code settings configured!

# Clean up the virtual environment (remove the venv folder)
clean:
	@echo Removing virtual environment...
	rmdir /s /q $(VENV_NAME)
	rmdir /s /q .vscode

# Activate the virtual environment and run the program
run:
	@echo Activating virtual environment and running the program...
	$(VENV_NAME)\Scripts\activate.bat && python main.py

# Run pylint on a specific file (pass FILE=your_script.py)
lint:
	@echo Running pylint on $(FILE)...
	@$(VENV_NAME)/Scripts/python -m pylint $(FILE)

# Run pylint on the entire project (cross-platform)
lint_all:
	@echo Running pylint on all Python files...
ifeq ($(OS),Windows_NT)
	@$(VENV_NAME)/Scripts/python -m pylint $(shell where /r . *.py)
else
	@$(VENV_NAME)/bin/python -m pylint $(shell find . -type f -name "*.py")
endif