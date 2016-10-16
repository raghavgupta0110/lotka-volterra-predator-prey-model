tec = generate_latex.tex
pic =phase_space_plot.png prey_and_predator.png parameters.tex

.PHONY: clean

generate_latex.pdf : $(tec) $(pic) prey_and_predator.blg\
		     prey_and_predator.bbl

	pdflatex $(tec)
	pdflatex $(tec)

prey_and_predator.blg prey_and_predator.bbl: sample.bib

	pdflatex $(tec)
	bibtex generate_latex

$(pic): python_plot.py

	python3 python_plot.py


clean :

	rm $(pic) *.aux *.lof *.log *.pdf *.toc *.bbl *.blg \
	*.out *~
