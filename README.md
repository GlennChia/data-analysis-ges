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

# 3. Useful Pandas commands

Remove rows with nan values within a specified column

```python
df.dropna(subset = [target_column], inplace=True)
```

Replace rows with nan values with a specified value within a specified column

```python
df[target_column].fillna(value, inplace=True)
```

# 4. Jupyter help

View function documentation by clicking `Shift Tab` while hovering over the function

