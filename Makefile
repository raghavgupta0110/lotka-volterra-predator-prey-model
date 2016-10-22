tec=source/generate_latex.tex
py_out=source/phase_space_plot.png source/prey_and_predator.png parameters.tex
ipyn=source/lotka_volterra_animation.ipynb
.PHONY: clean test

output/raghav_153079005.pdf : $(tec) $(py_out) source/lotka_volterra_animation.html \
		prey_and_predator.blg prey_and_predator.bbl

	pdflatex -jobname=153079005 $(tec)
	pdflatex -jobname=153079005 $(tec)
	mkdir -p output
	mv 153079005.pdf output/	
	mv source/lotka_volterra_animation.html output/153079005.html
source/lotka_volterra_animation.html: $(ipyn)

	jupyter nbconvert $(ipyn)
    
prey_and_predator.blg prey_and_predator.bbl: source/sample.bib

	pdflatex -jobname=153079005 $(tec)
	bibtex 153079005

$(py_out): source/python_plot.py

	python3 source/python_plot.py

open_pdf:

	evince 153079005.pdf

test:

	python3 source/python_plot_test.py

clean:
	rm -rf *.png *.tex *.aux *.toc *.bbl *.blg *.lof > /dev/null
	rm -rf *.log *.out output/ source/__pycache__ > /dev/null
