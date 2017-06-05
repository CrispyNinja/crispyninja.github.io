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

#cp debs/Packages .. && cp debs/Packages.bz2 .. && cp debs/Packages.gz ..

#rm debs/Packages && rm debs/Packages.bz2 && rm debs/Packages.gz

#for debs in *.deb
#do
#  rm debs
#done
