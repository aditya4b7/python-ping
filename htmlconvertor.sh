#! /bin/bash

html=index.html

echo "

<table border="1">
  <tr>
    <th>Source</th>
    <th>Destination</th>
    <th>Status</th>
  </tr>

" > index.html

    for file in `ls *.log` ; do

source=`awk '{print $3}' $file`
destination=`awk '{print $5}' $file`
status=`awk '{print $6}' $file`

if [ "$status" == "OK" ];then
echo "
  <tr>
    <td>$source</td>
    <td>$destination</td>
    <td bgcolor="#3CFF33">$status</td>
  </tr>
" >> index.html

elif [ "$status" == "FAILED" ];then
echo "
  <tr>
    <td>$source</td>
    <td>$destination</td>
    <td bgcolor="#FF4933">$status</td>
  </tr>
" >> index.html
fi

    done

echo "</table>" >> $html


