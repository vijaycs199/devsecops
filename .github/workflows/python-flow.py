name: Python Workflow Demo

on: [push]

jobs:
  Execute:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Python Version
        run: python -V
      - name: Identifying the Folder
        run: pwd
      - name: List the files in current directory
        run: ls ${{github.workspace}}
      - name: Run Python File
        run: python ../devsecops-cgi/hello.py
