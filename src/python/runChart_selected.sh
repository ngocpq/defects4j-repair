rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 3

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 5

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 7

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 9
rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools genprog -id 9

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 12

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 13

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 14
rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools genprog -id 14

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 15

rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools adqfix -id 18
rm -rf /tmp/torig*java
rm -rf /tmp/gzoltar.agent*.jar
python clear.py
python defects4j-repair.py -projects chart -tools genprog -id 18


