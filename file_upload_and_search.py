#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:43:46 2023

@author: Akshyat Patra
@College: Institute of Technical Education and Research

NOTE:
    Please install following libraries:
        tkinter: for GUI Layout --- pip install tkinter
        boto3: for api's' --- pip install boto3

"""

import tkinter as tk
from tkinter import *
import boto3


bucket_name = "comm050923"
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

s3_client = boto3.client(
    "s3",
    aws_access_key_id="AKIAYJQH7DJN3UXCRIQM",
    aws_secret_access_key="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",
)


def close_window():
    root.destroy()


def upload_file(event=None):

    email_id = email_id_entry.get()
    filename = str(filename_entry.get())

    key = email_id + "_" + filename

    testfile = "file.txt"
    with open(testfile, "a+") as f:
        f.write("This is a sample text For commvault")

    s3_client.upload_file("file.txt", "comm050923", key)

    # url = s3_client.generate_presigned_url(
    #     ClientMethod='get_object',
    #     Params={
    #         'Bucket': 'comm050923',
    #         'Key': key
    #     }
    # )

    # print(url)


def search_files(event=None):
    email_ids = email_ids_entry.get()
    search_query = str(search_query_entry.get())

    total = email_ids + "_" + search_query

    # s3 = boto3.client('s3')

    objects = s3_client.list_objects(Bucket=bucket_name)
    for object in objects["Contents"]:
        if object["Key"] == total:
            full_file_name = object["Key"]
            break

    # Download the file.
    output_label.config(text=full_file_name)


def down_files(event=None):
    file_name = output_label.cget("text")

    # s3_client.download_file(bucket_name, full_file_name, total)
    s3_client.download_file(bucket_name, file_name, file_name)
    openNewWindow()


def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("File Review")
    newWindow.geometry("300x200")

    Label(newWindow, text="File downloaded.").pack()


# Create the main window.
root = tk.Tk()

email_id_label = tk.Label(root, text="Email ID:")
email_id_entry = tk.Entry(root)


filename_label = tk.Label(root, text="Filename:")
filename_entry = tk.Entry(root)

email_ids_label = tk.Label(root, text="Email ID:")
email_ids_entry = tk.Entry(root)

search_query_label = tk.Label(root, text="Search file:")
search_query_entry = tk.Entry(root)

output_label = tk.Label(root, text="No files.")

# Buttons
upload_button = tk.Button(root, text="Upload", command=upload_file)
close_button = tk.Button(root, text="Close", command=close_window)
search_button = tk.Button(root, text="Search", command=search_files)
download_button = tk.Button(root, text="Download", command=down_files)


# Simple Layout
email_id_label.grid(row=0, column=0)
email_id_entry.grid(row=0, column=1)
filename_label.grid(row=1, column=0)
filename_entry.grid(row=1, column=1)
upload_button.grid(row=2, column=1)
email_ids_label.grid(row=3, column=0)
email_ids_entry.grid(row=3, column=1)
search_query_label.grid(row=4, column=0)
search_query_entry.grid(row=4, column=1)
search_button.grid(row=5, column=1)
output_label.grid(row=6, column=0)
download_button.grid(row=6, column=1)
close_button.grid(row=7, column=1)

# Start the main loop.
root.mainloop()
