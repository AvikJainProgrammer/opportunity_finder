# Makefile for setting up a Python virtual environment and installing dependencies

# Define the name of the virtual environment
VENV_NAME = venv

# Define the Python interpreter (you can specify python3 if needed)
PYTHON = python

# Default target
all: venv install

# Create a virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_NAME)
	@echo "Virtual environment created at $(VENV_NAME)/"

# Install dependencies from requirements.txt
install: venv
	@echo "Activating virtual environment and installing dependencies..."
	@source $(VENV_NAME)/bin/activate && pip install -r requirements.txt

# Clean up the virtual environment (remove the venv folder)
clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_NAME)

# Deactivate the virtual environment
deactivate:
	@echo "To deactivate, simply run 'deactivate' in your terminal."

