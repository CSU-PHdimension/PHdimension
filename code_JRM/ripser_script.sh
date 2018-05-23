#!/bin/bash
# Settings:
beg=50
inc=50
end=100
dimn=2
for (( i=$beg; i<=$end; i+=$inc))
do
   file=pointsUnitCub_$i.csv  # TODO: Edit this line to match filename format!
   echo "Computing homology of $file"
   outfn=Homology_$i.txt
   ripser $file --format point-cloud --dim $dimn >$outfn
done
