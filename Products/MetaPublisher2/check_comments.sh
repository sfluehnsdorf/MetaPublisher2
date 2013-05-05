grep -rh \!TXT\! *
echo
grep -rc \!TXT\! * | grep -v ":0$" | sort -n -k2 -t:
echo
grep -rhc \!TXT\! * | grep -v ":0$" | awk '{ count += $0} END {print count}'
