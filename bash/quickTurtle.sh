#!/bin/bash

URL='http://85.25.211.218/downloads/War-Dogs-2016-720p-hdpopcorns.mp4?st=5Vwd2hxzCXG6ghVRnGtsQQ&e=1543070953'
echo $(curl -sI $URL | grep -i Content-Length | awk '{print $2}')
read TOTLENGTH
THREADS=16
AVGLENGTH=$TOTLENGTH/$THREADS
DOWNRANGE=0
UPRANGE=$((DOWNRANGE+AVGLENGTH))

for i in {1..16}; do
echo '#!/bin/bash' > "$i.sh";
echo "URL='$URL'" >> "$i.sh";

if (($i == 16)); then echo "curl -s -r $DOWNRANGE- \$URL -o part$i" >> "$i.sh";
elif (($i !=16)); then echo "curl -s -r $DOWNRANGE-$UPRANGE \$URL -o part$i" >> "$i.sh"; fi

DOWNRANGE=$((UPRANGE+1));
UPRANGE=$((UPRANGE+AVGLENGTH));
chmod +x "$i.sh";
bash "$i.sh" &
done
