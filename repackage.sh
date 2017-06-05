#!/bin/bash
echo "Repackaging..."

rm Packages.bz2 #&& rm Packages.gz

bzip2 < Packages > Packages.bz2 #&& gzip < Packages > Packages.gz

rm Packages

echo "Done!"
