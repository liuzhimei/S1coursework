# S1 Coursework

This repository contains the code and dependencies required for running the `S1_coursework.ipynb` Jupyter Notebook. Follow the steps below to set up the environment and run the notebook.

**Note**: This is the assessed coursework for the course **Statistical Methods in Data Intensive Science**, which is one of the courses of the Data Intensive Science Mphil programme, at the University of Cambridge. The questions are listed in the file `S1_Coursework_Questions.pdf`, and my report is the file `S1_coursework_report.pdf`.

---

## 1. Environment Setup

To ensure all dependencies are installed properly, set up the environment using the provided `environment.yml` file.

### Prerequisites

- Install **Anaconda** or **Miniconda** from [Anaconda's official website](https://www.anaconda.com/products/individual) or [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).
- Verify `conda` installation by running:
   ```bash
   conda --version
   ```
### Steps to Create the Environment
Run the following commands in terminal:
1. Clone the repository
    ```bash
    git clone git@gitlab.developers.cam.ac.uk:phy/data-intensive-science-mphil/assessments/s1_coursework/zl474.git
    cd zl474
    ```
2. Create the environment from the `environment.yml` file:
    ```bash
    conda env create -f environment.yml
    ```
3. Confirm the environment was created successfully:
    ```bash
    conda env list
    ```

## 2. Activate the Environment
1. Before running the notebook, activate the environment:
    ```bash
    conda activate S1_zhimei_env
    ```
2. Install Jupyter in the environment using:
    ```bash
    pip install jupyter
    ```
3. Install the `ipykernel` package using:
    ```bash
    pip install ipykernel
    ```
4. To make sure the environment can be run in Jupyter notebook, you need to add the environment as a kernel to Jupyter:
    ```bash
    python -m ipykernel install --user --name S1_zhimei_env --display-name "Python (S1_zhimei_env)"
    ```

## 3. Run Jupyter Notebook
1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
2. Navigate to the folder containing `S1_coursework.ipynb` in the Jupyter Notebook interface.
3. Open the `S1_coursework.ipynb` notebook.
4. Run the notebook cells step-by-step to execute the code.