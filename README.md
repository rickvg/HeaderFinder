## Header Finder

A program used to find file signatures in raw data to identify files. 
This Python program supports multiprocessing and is able to process multiple files at once.

## Usage

Usage when using the Python version is:

`python HeaderFinder.py [file1] [file2] etc.`

## Results

This program shows the results per file in a separate textfile. It contains the hexadecimal value of the signature, the binary value of the signature and the location of the signature in the raw data.
For now you can scan the file signature in a file signature database to check what kind of file it belongs to.

## Adding files to the database

Currently, the database is a TXT-file containing hexadecimal values. To add a value, simply add a new line:

`[Hexadecimal file signature]`