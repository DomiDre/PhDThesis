pdflatex dresen_thesis
cp dresen_thesis.pdf last_build.pdf
biber dresen_thesis
makeglossaries dresen_thesis
pdflatex dresen_thesis.tex
cp dresen_thesis.pdf last_build.pdf