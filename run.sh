#!/bin/bash


export ASTOR_HOME=~/astor
#export ASTOR_JAR=${ASTOR_HOME}/target/astor-0.0.2-SNAPSHOT-jar-with-dependencies.jar
export EXPERIMENT_ROOT=${ASTOR_HOME}/experiments/defects4j-repair

bugId=5
projId=math
tool=adqfix
timeout=10000

#run project Chart, bug id

echo "time python ${EXPERIMENT_ROOT}/src/python/defects4j-repair.py -project ${projId} -tools ${tool} -id ${bugId} --timeout ${timeout}"

time python ${EXPERIMENT_ROOT}/src/python/defects4j-repair.py -project ${projId} -tool ${tool} -id ${bugId} --timeout ${timeout}


