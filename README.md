![Screenshot](logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/pypi.svg?branch=master)](https://travis-ci.org/vyahello/pypi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![Docker pulls](https://img.shields.io/docker/pulls/vyahello/pypi.svg)](https://hub.docker.com/repository/docker/vyahello/pypi)


# PYPI clone

> A clone of https://pypi.org based on **fastAPI** python web framework.

## Tools

### Production
- 3.7, 3.8, 3.9
- [fastapi](https://fastapi.tiangolo.com/)

### Development

- [travis](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [flake8](http://flake8.pycqa.org/en/latest/)

## Usage

Please check deployed pypi app via:
  - https://pypi-clone.herokuapp.com (prod stage)
  - http://178.62.222.165:5004 (test stage)

![Demo](intro.gif)

### Docker run

```bash
docker run -it -p 8080:8080 vyahello/pypi:0.1.0
```

Then please open http://0.0.0.0:8080 in your browser.

### Source code

```bash
git clone git@github.com:vyahello/pypi-fastapi-clone.git
python3 -m venv venv 
. venv/bin/activate
cd pypi
pip install -r requirements.txt
python -m pypi
```

Then please open http://0.0.0.0:8080 in your browser.

**[⬆ back to top](#pypi-clone)**

## Development notes

### Docker image build

Please refer to docker image build procedure at [fast-weather-api-docker](https://github.com/vyahello/fast-weather-api#docker-image-build)

### Linux deployment

Please refer to linux deployment procedure at [fast-weather-api-deployment](https://github.com/vyahello/fast-weather-api#deployment)

### Load PYPI DB

```bash
python pypi/bin/load_db.py
```

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run unittests:
```bash
pytest
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `flake8`, `mypy`) and unittests (`pytest`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```
### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Vladimir Yahello_. Please check [authors](AUTHORS.md) file for more details.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/pypi/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#pypi-clone)**
