for var in "$@"
do
	echo "$var"
	rm -rf /tmp/torig*java
	rm -rf /tmp/gzoltar.agent*.jar
	python clear.py
	python defects4j-repair.py -projects chart -tools adqfix -id $var
	rm -rf /tmp/torig*java
	rm -rf /tmp/gzoltar.agent*.jar
	python clear.py
	python defects4j-repair.py -projects chart -tools genprog -id $var

done
