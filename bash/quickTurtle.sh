#!/bin/bash

URL='INSERT_YOUR_URL_HERE'
echo $(curl -sI $URL | grep -i Content-Length: | awk '{print $2}')
#input is prompted, write the numerical value on the screen and press enter.
echo 'enter the number shown'
read TOTLENGTH
THREADS=16
AVGLENGTH=$TOTLENGTH/$THREADS
DOWNRANGE=0
UPRANGE=$((DOWNRANGE+AVGLENGTH))

for i in {1..$THREADS}; do
echo '#!/bin/bash' > "$i.sh";
echo "URL='$URL'" >> "$i.sh";

if (($i == $THREADS)); then echo "curl -s -r $DOWNRANGE- \$URL -o part$i" >> "$i.sh";
elif (($i != $THREADS)); then echo "curl -s -r $DOWNRANGE-$UPRANGE \$URL -o part$i" >> "$i.sh"; fi

DOWNRANGE=$((UPRANGE+1));
UPRANGE=$((UPRANGE+AVGLENGTH));
chmod +x "$i.sh";
bash "$i.sh" &
done
