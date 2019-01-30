### Deploying the Project
Follow these steps in order to deploy it correctly via Python VirtualEnviroment.
 1. Setup and configure [Python 3.6](https://www.python.org/downloads/release/python-360/) and python3-pip
 2. Install some libraries which will help to compile tensorflow file during installation
    ```bash
        apt-get install python3-dev g++ build-essentials
 3. Install Virtual Enviroment globally
    ```bash
        sudo apt-get install virtualenv
    ```
4. Create virtual enviroment for the app by navigating into app directory
    ```bash
       virtualenv --python=python3 venv
    ```
5. Activate the virtual enviroment
    ```bash
       sources venv/bin/activate
    ```
6. Install the required packages
    ```bash
       pip install -r requirements.txt
    ```
7. Running Server (run.py file is inside the server folder)
    ```python
       python run.py
    ```
