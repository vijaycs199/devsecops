name: Python Workflow Demo

on: [push]

jobs:
  Build:
    runs-on: ubuntu-latest
    steps:
      - name: Building the Code
        run: echo "Building the Code"
      - name: Wait for the Code Building
        run: sleep 30

  Execute:
    runs-on: ubuntu-latest
    needs: Build
    steps:
      - name: Run Python File
        run: python hello.py
