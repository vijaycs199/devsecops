name: execute java file
  
on: [push]

jobs:
  Execute: 
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: python version check
        run: python -V
      - name: Identifying the folder
        run: pwd
      - name: list the files from current directory
        run: ls ${github.workspace}
      - name: Run java file
        run: javac ../devsecops/hello.java
