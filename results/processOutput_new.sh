echo "Patches info:"

logFile=./**/*/stdout.log.full

grep -r -m 1 -B 1 "isSolution: true" ${logFile} | grep "Variant id: " > firstSolution.txt

grep -r -m 1 -A 1 "Patch 1" ${logFile} | grep "VARIANT_ID=" > firstSolution_2.txt

grep -r -c "isSolution: true" ${logFile} > countSolution.txt

echo "output status:"
grep -r "OUTPUT_STATUS=" ${logFile} > outputStatus.txt

grep -r "TOTAL_TIME=" ${logFile} > totalTime.txt

grep -r "NR_GENERATIONS=" ${logFile} > nr_generation.txt

grep -r "NR_RIGHT_COMPILATIONS=" ${logFile} > nr_right_compilation.txt

grep -r "NR_FAILLING_COMPILATIONS=" ${logFile} > nr_failing_compilation.txt

#grep -r "NR_FAILING_VALIDATION_PROCESS=" * 


