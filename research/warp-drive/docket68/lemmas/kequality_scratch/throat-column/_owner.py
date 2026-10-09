"""Load the owners by path (never copied): lemmas/sim2_facing.py and lemmas/b6_k.py."""
import contextlib, importlib.util, io, os, sys
D68 = "/home/user/Claude-Method-Works/research/warp-drive/docket68"
LEM = os.path.join(D68, "lemmas")
WD = os.path.dirname(D68)


def load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


_SIM2 = None


def sim2():
    global _SIM2
    if _SIM2 is None:
        _SIM2 = load(os.path.join(LEM, "sim2_facing.py"), "tc_sim2_facing")
    return _SIM2
