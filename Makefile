VERILATOR = verilator
TOP = tb_fir
RTL = rtl/fir.sv
TB = tb/tb_fir.sv
CPP = sim_main.cpp

VFLAGS = --timing -Wall -Wno-fatal --cc --exe --build

all: sim

sim:
	$(VERILATOR) $(VFLAGS) $(RTL) $(TB) $(CPP) --top-module $(TOP)
	./obj_dir/V$(TOP)

clean:
	rm -rf obj_dir