# Crowdbotics Lite

## Api Documentation

- use this [link](http://localhost:8000/) to access the api documentation

> ## How to set up the project

### Features

- python 3.10
- [poetry](https://python-poetry.org/docs/) as dependency manager

---

### PROJECT SETUP

- clone the repository

```bash
https://github.com/crowdbotics-lite .git
```

- cd into the directory

```bash
cd crowdbotics-lite
```

### create environment variables

On Unix or MacOS, run:

```bash
cp .env.example .env
```

You can edit whatever values you like in there.

Note: There is no space next to '='

### On terminal

```bash
source .env
```

---

> > ### VIRTUAL ENVIRONMENT

---

**To Create/Activate:**

```bash
make activate
```

**Installing dependencies:**

```bash
make install
```

> > ### MIGRATIONS - DATABASE

---

#### Make migrations

```bash
make makemigrations
```

---

#### Update DB with the latest migrations

```bash
make migrate
```

---

> > ### THE APPLICATION

---

#### run application

```bash
make run
```
