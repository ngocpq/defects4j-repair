echo "Patches info:"

grep -r -m 1 -B 1 "isSolution: true" * | grep "Variant id: " > firstSolution.txt

grep -r -m 1 -A 1 "Patch 1" * | grep "VARIANT_ID=" > firstSolution_2.txt

grep -r -c "isSolution: true" * > countSolution.txt

echo "output status:"
grep -r "OUTPUT_STATUS=" * > outputStatus.txt

grep -r "TOTAL_TIME=" * > totalTime.txt

grep -r "NR_GENERATIONS=" * > nr_generation.txt

grep -r "NR_RIGHT_COMPILATIONS=" * > nr_right_compilation.txt

grep -r "NR_FAILLING_COMPILATIONS=" * > nr_failing_compilation.txt

#grep -r "NR_FAILING_VALIDATION_PROCESS=" * 


