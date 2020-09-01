# 1. Data Source

Refer to [https://data.gov.sg/dataset/graduate-employment-survey-ntu-nus-sit-smu-suss-sutd?resource_id=9326ca53-9153-4a9c-b93f-8ae032637b70](Graduate Employment Survey - NTU, NUS, SIT, SMU, SUSS & SUTD) for the data

# 2. Conda commands and setup

Create a conda envrionment based on an `environment.yml` file

```bash
conda env create -f environment.yml
```

List environments

```bash
conda list
```

Remove environment

```bash
conda remove --name ENVNAME --all
```

Activate environment

```bash
conda activate data-analysis-ges
```

Start Jupyter notebook

```bash
jupyter lab
```