#!/bin/bash
# Settings:
beg=50
inc=50
end=10000
dimn=1
for (( i=$beg; i<=$end; i+=$inc))
do
   file=UnitTriangle/points_$i.csv  # Edit this line to match filename format!
   echo "Computing homology of $file"
   date
   outfn=UnitTriangle/Homology_$i.txt # Edit this line to match filename format!
   ripser $file --format point-cloud --dim $dimn >$outfn
done
