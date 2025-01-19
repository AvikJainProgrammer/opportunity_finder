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

# Clean up the virtual environment (remove the venv folder)
clean:
	@echo Removing virtual environment...
	rmdir /s /q $(VENV_NAME)

