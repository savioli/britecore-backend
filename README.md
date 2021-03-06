# BriteCore FrontEnd

<div>
  <span>
    <img src="https://img.shields.io/badge/PEP8-Compliant-20b120.svg">
  </span> 
  <span>
    <img src="https://img.shields.io/badge/lint-flake8-0044ff.svg">
  </span>
  <span>
    <img src="https://img.shields.io/badge/imports-isort-ff3300.svg">
  </span>
  <span>
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </span>
</div>

</br>

**This repository is part of **[BriteCore Hiring Project](https://github.com/savioli/britecore-hiring-project.git)**.**

It contains the base code for the **BriteCore BackEnd**.

## Stack

This project is based on **[Python 3.9.2](https://apijs.org/)** + **[Django 3.1.7](https://nodejs.org/)** + **[Postgres 13.2](#)** using **LTS** versions of each technology.  

## Getting Started

### **Requirements**
- [Docker](https://docs.docker.com/install/) **for development and production environments**
- [Docker Compose](https://docs.docker.com/compose/install/) **for development and production environments**
- [Docker Compose CLI](https://github.com/docker/compose-cli) **for the production environment only**

## Environments

The **Development Environment** runs in **Docker** orchestrated with **Docker Compose**.  

The **Production Environment** is orchestrated with **AWS CloudFormation** using **AWS ECS and Fargate**.  

## Code Quality

The repository uses **[pre-commit]()** with **[flake8](#)**, **[isort](#)**, and **[black](#)** to enforce style guide and to perform static code analysis to identify problematic patterns and avoid antipatterns as well as enforcing the **PEP8 compliance**.


## Development Environment

To set up the development environment follow the steps of the guide below.

### Setting Up the Development Environment

To have the development environment running you will need **Docker** and **Docker Compose** installed.

### 1 Development Environment Initialization

Inside of **britecore-backend**.

1. Build the Docker containers using:

```bash
docker-compose build
```

2. Start the development environment using:

```bash
docker-compose up
```

The application will be running at [http://localhost:8000](http://localhost:8000).

## Common Commands

Here are some most frequently used commands used during the development process.

### Access the container
```
docker-compose run --rm api sh
```

### Run manage.py commands
```
docker-compose run --rm api python manage.py <command>
```
###### Example:
```
docker-compose run --rm api python manage.py test
```
---

For more information do not hesitate to contact me with any additional questions or comments at **andre_savioli@hotmail.com**.
