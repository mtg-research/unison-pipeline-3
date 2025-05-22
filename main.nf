#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.data_file = 'data.yaml'
params.out_dir = 'results'

process runPythonExample {
    publishDir '.', mode: 'copy'
    tag 'Run python-example container'

    container 'python:3.11'

    input:
    path data_file
    path query_py

    output:
    path 'result.txt', emit: result

    script:
    """
    mkdir -p /data
    cp ${data_file} /data/data.yaml
    pip3 install pyyaml
    python3 ${query_py} /data/data.yaml /data/result.txt
    cp /data/result.txt result.txt
    """
}

workflow {
    runPythonExample(file(params.data_file), file('query.py'))
}