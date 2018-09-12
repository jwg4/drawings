all: image.pdf

clean:
	rm *.pdf
	rm skyline.tex

image.pdf: image.tex skyline.tex
	pdflatex image.tex

skyline.tex: drawing.py
	python drawing.py > skyline.tex
