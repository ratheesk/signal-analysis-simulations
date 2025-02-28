# Wave Modulation Flask Web App

This is a simple Flask web app to interactively learn about **Continuous Wave Modulation** and **Pulse Modulation**, along with various sub-chapters related to these topics.

## Project Setup

### Prerequisites

Make sure you have **Conda** installed on your system. You can download Conda from the official site: [Conda Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Steps to Set Up the Project

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
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

4. **Run the Flask app**:
   After setting up the environment, you can run the Flask app with the following command:

   ```bash
   python app.py
   ```

5. **Access the app**:
   Open your browser and go to `http://127.0.0.1:8050/` to interact with the app.

### Development

1. Export the environment to environment.yml: After installing the required packages, you can export the environment configuration into an environment.yml file to share or replicate the environment.

   ```bash
   conda env export > environment.yml
   ```

2. Create a requirements.txt file: Once the necessary packages are installed, generate a requirements.txt file:

   ```bash
   pip freeze > requirements.txt
   ```
