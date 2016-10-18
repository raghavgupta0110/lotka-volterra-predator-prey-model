tec = generate_latex.tex
pic = phase_space_plot.png prey_and_predator.png parameters.tex

.PHONY: clean

generate_latex.pdf : $(tec) $(pic) lotka_volterra_animation.html \
                    prey_and_predator.blg prey_and_predator.bbl

	pdflatex $(tec)
	pdflatex $(tec)
	

lotka_volterra_animation.html: $(lotka_volterra_animation.ipynb)

	jupyter nbconvert lotka_volterra_animation.ipynb
    
prey_and_predator.blg prey_and_predator.bbl: sample.bib

	pdflatex $(tec)
	bibtex generate_latex

$(pic): python_plot.py

	python3 python_plot.py

clean:
	rm -r $(pic) generate_latex.aux generate_latex.lof \
	generate_latex.log generate_latex.toc generate_latex.bbl \
	generate_latex.blg generate_latex.out
