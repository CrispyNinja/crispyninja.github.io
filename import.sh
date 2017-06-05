#!/bin/bash
rm Packages && rm Packages.bz2 && rm Packages.gz

for debs in debs/*.deb
do
  rm $debs
done

for d in debs/*/
do
  dpkg -b $d
done

dpkg-scanpackages debs/ /dev/null > Packages && bzip2 < Packages > Packages.bz2 && gzip < Packages > Packages.gz
