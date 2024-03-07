#Makefile

.PHONY: export

export:
	jinja2 --format=yaml template/template.j2 output.yml -o README.md
