# Build outside the repository: make BUILD=/some/dir   (default /tmp/rule-build)
BUILD ?= /tmp/rule-build
SOLVER ?= ../solver
CXX ?= g++
CXXFLAGS ?= -O3 -march=x86-64-v3 -std=c++17 -fopenmp -Wall -Wno-unused-variable -Wno-unused-but-set-variable
GMPLIB := $(shell for d in /usr/lib/x86_64-linux-gnu /usr/lib64 /usr/lib /usr/local/lib; do [ -e $$d/libgmp.so ] && echo -lgmp && exit; done; echo -l:libgmp.so.10)
HDRS = fixp.h gmpmin.h exactfn.h matrices.h cell.h scheme.h sha256.h $(SOLVER)/rhs_gen.h

all: $(BUILD)/rule $(BUILD)/t_fixp
$(BUILD)/rule: rule.cpp $(HDRS)
	@mkdir -p $(BUILD)
	$(CXX) $(CXXFLAGS) -I. -I$(SOLVER) -o $@ rule.cpp $(GMPLIB)
	@sha256sum $(SOLVER)/rhs_gen.h
$(BUILD)/t_fixp: tests/t_fixp.cpp fixp.h gmpmin.h
	@mkdir -p $(BUILD)
	$(CXX) -O2 -std=c++17 -I. -o $@ tests/t_fixp.cpp $(GMPLIB)
clean:
	rm -rf $(BUILD)
