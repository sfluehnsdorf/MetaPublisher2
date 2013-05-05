grep -rh \!\!\! *
echo
grep -rc \!\!\! * | grep -v ":0$" | sort -n -k2 -t:
echo
grep -rhc \!\!\! * | grep -v ":0$" | awk '{ count += $0} END {print count}'
