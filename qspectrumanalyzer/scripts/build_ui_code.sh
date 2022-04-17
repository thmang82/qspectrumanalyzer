outfolder="./"

FILES=$(ls qspectrumanalyzer*.ui)
for i in $FILES ; do
  outfile=$outfolder"ui_"`basename $i .ui`.py
  echo $i
  echo $outfile
  pyuic5 -o $outfile $i
done