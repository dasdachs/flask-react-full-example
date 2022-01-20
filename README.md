# Flask + ReactJS full example

This is an example [ReactJs](https://reactjs.org/) app with a [Flask](https://flask.palletsprojects.com/en/2.0.x/) backend acting as a [Rest API](https://www.redhat.com/en/topics/api/what-is-a-rest-api).

The app is used for inventory tracking. User can keep a list of their inventory, or they can add inventories to existing, public ones.

## Develop

## Dependencies

1. The project uses [Python 3.9](https://www.python.org/) or higher, [NodeJs 16](https://nodejs.org/en/) and [Docker](https://www.docker.com/).
   
2. We use [Npm](https://www.npmjs.com/) - installed with Node -  and [Poetry](https://python-poetry.org/) to manage Python packages and create the virtual environment. 
   Since _Poetry_ is not installed Install with Python, make sure to install it before starting the project.


### Setup the project locally

```bash
# Clone the code
git clone https://github.com/dasdachs/flask-react-full-example .
cd flask-react-full-example
```

# install the root dependencies to setup and run the project

```bash
npm install             # installs the root project dependencies
npm run bootstrap       # installs the package dependencies and create a virtual environment
```

### Start the databases

```bash
docker-compose up -d    # omit the -d flag if you want to see the stdout output
```

## Start the app

```bash
npm start               # run npm run start:server or :client to run only once part of the app
```

