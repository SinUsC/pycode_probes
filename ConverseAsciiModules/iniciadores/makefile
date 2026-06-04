PYTHON=python3
SCRIPT=cli_runner.py
IMAGE=img/Diseno-sin-titulo-3.jpg
WIDTH=100
CONTRAST=2.0
SIGNATURE=GRX
OUTPUT=img/output/arte_grx.txt
SHOW=true

all: run

run:
    $(PYTHON) $(SCRIPT) -i $(IMAGE) -w $(WIDTH) -c $(CONTRAST) -s $(SIGNATURE) -o $(OUTPUT) $(if $(SHOW),-v)

install:
    pip install pillow numpy

clean:
    rm -f $(OUTPUT)

.PHONY: all run install clean
