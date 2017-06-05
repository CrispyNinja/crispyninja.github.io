#!/bin/bash
for d in */
do
  dpkg -b $d
done

dpkg-scanpackages . /dev/null > Packages && bzip2 < Packages > Packages.bz2 && gzip < Packages > Packages.gz

cp Packages .. && cp Packages.bz2 .. && cp Packages.gz ..
