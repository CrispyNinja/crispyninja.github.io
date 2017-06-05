#!/bin/bash
rm Packages && rm Packages.bz2 && rm Packages.gz

#for debs in debs/*.deb
#do
#  rm $debs
#done

#for d in debs/*/
#do
#  dpkg -b $d
#done

for d in debs/*.deb
do
  echo "Found deb: $d"
done

dpkg-scanpackages debs/ /dev/null > Packages && bzip2 < Packages > Packages.bz2 && gzip < Packages > Packages.gz
