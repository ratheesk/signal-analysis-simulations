# Signal Analysis Simulations

[![License](https://img.shields.io/github/license/ratheesk/signal-analysis-simulations.svg)](https://github.com/ratheesk/signal-analysis-simulations/blob/master/LICENSE)

This is an interactive web app to explore about signal analysis and simulation., along with various sub-chapters related to these topics. The app is developed using **Dash**.

## Project Setup

### Prerequisites

Ensure that you have **Python** installed on your system. Optionally, you can use **Conda** for managing environments.

- **Python**: [Download Python](https://www.python.org/downloads/)
- **Conda (optional)**: [Conda Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

### Steps to Set Up the Project

#### Option 1: Using Conda (Optional)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ratheesk/signal-analysis-simulations.git
   cd wave-modulation
   ```

2. **Create and activate the Conda environment**:
   Create a new Conda environment using the provided `environment.yml` file. This file contains the necessary dependencies for the project.

   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment**:
   Once the environment is created, activate it by running:

   ```bash
   conda activate wave-modulation
   ```

4. **Run the Dash app**:
   The app is located inside the `src` folder. Navigate to that folder and then run the app using the following command:

   ```bash
   cd src
   python app.py
   ```

#### Option 2: Using Virtualenv (If not using Conda)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ratheesk/signal-analysis-simulations.git
   cd wave-modulation
   ```

2. **Create a virtual environment**:
   Create a new virtual environment using `virtualenv` or `venv` (for Python 3.3+):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   Install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Dash app**:
   The app is located inside the `src` folder. Navigate to that folder and then run the app using the following command:

   ```bash
   cd src
   python app.py
   ```

6. **Access the app**:
   Open your browser and go to `http://127.0.0.1:8050/` to interact with the app.

### Development

1. **Export the environment to environment.yml** (Conda users): After installing new packages or updating dependencies, export the environment configuration into an `environment.yml` file to share or replicate the environment.

   ```bash
   conda env export > environment.yml
   ```

2. **Update the `requirements.txt` file**: If you install additional packages using `pip` or update the environment, generate an updated `requirements.txt` file for Python virtual environments:

   ```bash
   pip freeze > requirements.txt
   ```

3. **Adding New Packages**: If you add any new dependencies to the project, remember to update both the `environment.yml` file (for Conda users) and the `requirements.txt` file (for `pip` users) to ensure proper environment reproduction.
