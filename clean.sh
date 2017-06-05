#delete all .DS_Store
for ds in */.DS_Store
do
  rm $ds
done

for ds in */*/.DS_Store
do
  rm $ds
done
