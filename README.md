# README
This Python code is a simple file upload and search application that uses the boto3 library to interact with Amazon S3.

## Requirements
- Python 3.8 or higher
- tkinter library
- boto3 library

## Installation
To install the required libraries, run the following commands in your terminal:
```bash
pip install tkinter
pip install boto3
```
## Usage
To run the application, open a terminal and navigate to the directory where the code is located. Then, run the following command:
```bash
python3 file_upload_and_search.py
```
- The application will open a window with two text boxes and four buttons. The text boxes are used to enter the email ID and filename of the file to upload. The buttons are used to upload the file, search for files, download a file, and close the application.

#### Uploading a file
- To upload a file, enter the email ID and filename in the text boxes and then click the "Upload" button. The file will be uploaded to the Amazon S3 bucket named "comm050923".

#### Searching for files
- To search for files, enter the email ID and search query in the text boxes and then click the "Search" button. The application will search for files in the Amazon S3 bucket that match the search query. The full filename of the first matching file will be displayed in the output label.

#### Downloading a file
- To download a file, click the "Download" button. The file will be downloaded to the current working directory.

#### Closing the application
- To close the application, click the "Close" button.

I hope this is helpful!

