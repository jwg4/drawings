all: image.pdf

clean:
	rm *.pdf
	rm skyline.tex

image.pdf: image.tex skyline.tex
	pdflatex image.tex

skyline.tex: drawing.py
	python make_drawing_code.py > skyline.tex
