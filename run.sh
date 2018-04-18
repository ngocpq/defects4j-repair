#!/bin/bash


export ASTOR_HOME=~/astor
#export ASTOR_JAR=${ASTOR_HOME}/target/astor-0.0.2-SNAPSHOT-jar-with-dependencies.jar
export EXPERIMENT_ROOT=${ASTOR_HOME}/experiments/defects4j-repair

bugId=2
projId=Chart
tool=genprog
timeout=10000

#run project Chart, bug id


time python ${EXPERIMENT_ROOT}/src/python/defects4j-repair.py -project ${projId} -tool ${tool} -id ${bugId} --timeout ${timeout}


