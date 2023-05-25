# poc-upload-manager
This project provides a simple way to upload files to a MinIO server using a web interface. The project consists of two main components: a web interface for uploading files, and a collector that periodically scans a directory for new files and uploads them to the MinIO server.
## Containers directory
The containers directory contains the Dockerfiles and configuration files necessary to build and run the project in a containerized environment. There are two subdirectories:

   - web: contains the Dockerfile and configuration files for the MinIO web interface.
   - collector: contains the Dockerfile and configuration files for the collector.


## Collector
The app.py script inside the collector is responsible for scanning the directory for new files and uploading them to the MinIO server. The script uses the MinIO Python SDK to interact with the server.

## Creating a virtual environment
To create a virtual environment using venv, follow these steps:


#### Run the following command to create a new virtual environment:
*Open a terminal window and navigate to the directory where you want to create the virtual environment.*

``` 
python -m venv env-miniocollector
``` 
This will create a new directory called myenv in the current directory, which contains the Python executable and other files needed for the virtual environment.

#### Activate the virtual environment by running the following command:

``` 
source env-miniocollector/bin/activate
``` 
This will activate the virtual environment and change your prompt to indicate that you are now working inside the virtual environment.

#### Install the necessary packages using pip:

``` 
pip install docker-compose django-bootstrap-v5 watchdog loguru
``` 
*This will install the depedenvies of packages inside the virtual environment.*

### Starting the container
#### To start the container, run the following command:

```
docker-compose --env-file .env -f containers/compose-base.yaml up --build
```
*This will start both the web interface and the collector.*
