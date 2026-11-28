# Build outside the repository: make BUILD=/some/dir   (default /tmp/rule-build)
BUILD ?= /tmp/rule-build
SOLVER ?= ../solver
CXX ?= g++
CXXFLAGS ?= -O3 -march=x86-64-v3 -ffp-contract=off -fno-fast-math -std=c++17 -fopenmp -Wall -Wno-unused-variable -Wno-unused-but-set-variable
# -ffp-contract=off and no -ffast-math are part of the rule: the short arithmetic is binary64 with every operation
# rounded once (no fused multiply-add, no reordering); x86-64 doubles are SSE2 (no extended precision).
GMPLIB := $(shell for d in /usr/lib/x86_64-linux-gnu /usr/lib64 /usr/lib /usr/local/lib; do [ -e $$d/libgmp.so ] && echo -lgmp && exit; done; echo -l:libgmp.so.10)
HDRS = fixp.h gmpmin.h exactfn.h matrices.h cell.h scheme.h sha256.h $(SOLVER)/rhs_gen.h

all: $(BUILD)/rule $(BUILD)/t_fixp
$(BUILD)/rule: rule.cpp $(HDRS)
	@mkdir -p $(BUILD)
	$(CXX) $(CXXFLAGS) -I. -I$(SOLVER) -o $@ rule.cpp $(GMPLIB)
	@sha256sum $(SOLVER)/rhs_gen.h
$(BUILD)/t_fixp: tests/t_fixp.cpp fixp.h gmpmin.h
	@mkdir -p $(BUILD)
	$(CXX) $(CXXFLAGS) -I. -o $@ tests/t_fixp.cpp $(GMPLIB)
clean:
	rm -rf $(BUILD)
