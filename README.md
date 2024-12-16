# kaggle

## workflow
1. create new project's branch
    - main
    - dev
    - project
        - feature
            - worker
1. create new project's directories
    - project_root
        - environments
            - prod
            - dev
            - exp
                - project
                    - Dockerfile
                    - docker-compose.yaml
                    - poetry.lock
                    - pyproject.toml
        - src
            - {modules}
            - projects
                - {project}
                    - EDA.ipynb
                    - ...
            - main.py (train schedule)
    - DATA_DIR
        - {project}
            - raw
            - ...
2. decide python version and
    - ```pyenv install {version}```
    - ```pyenv local {version}```
    - ```cd {project env directory}```
    - ```poetry init```
    - ```poetry env use $(pyenv which python)```
3. (option) add kernel
    - install jupyter
    - ```poetry shell```
    - ```poetry add ipykernel```
    - ```poetry run python -m ipykernel install --user --name {kernel name}```
4. EDA
5. baseline
6. do experiments
7. upgrade modules
