class A(object):
    explanation_ = AttributeError("aaaaaaa")
    
    
    def __getattr__(self, attr):
        try:
            obj = getattr(None, 'request')
        except AttributeError:
            raise self.explanation_
        return getattr(obj, attr)


ra = A()

class B(object):
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None
    
    def set_ref(self, ref):
        self.ref = ref

class C(object):
    def __init__(self, obj) -> None:
        self.data = [obj]

# wb = None
# wc = None

def test_increase_2(n=10000000):
    xx = ['1'] * n
    b = B(xx)
    c = C(b)
    b.set_ref(c)
    # global wb, wc
    # wb = weakref.ref(b)
    # wc = weakref.ref(c)
    hasattr(ra, 'headers')


import gc
gc.freeze()

test_increase_2()

frame = A.explanation_.__context__.__traceback__.tb_frame.f_back

# observer ref
import weakref
rf = [weakref.ref(i) for i in gc.get_referents(frame) if i.__class__.__module__ not in ['builtins', 'weakref']]

frame.clear()

import gc
# gc.set_debug(gc.DEBUG_LEAK)
gc.collect()


