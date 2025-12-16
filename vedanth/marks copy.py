"""
This is for Method Resolution Order where we get the output based on First Match.
"""
# ============================================================
# 1. ROOT CLASS (end of chain)
# ============================================================

class Root:
    def __init__(self):
        print("Root.__init__")
        super().__init__()

    def process(self):
        print("Root.process (should rarely be seen)")


# ============================================================
# 2. MIXINS (same method name, cooperative design)
# ============================================================

class LoggerMixin(Root):
    def __init__(self):
        print("LoggerMixin.__init__")
        super().__init__()

    def process(self):
        print("LoggerMixin.process → logging")
        super().process()


class AuthMixin(Root):
    def __init__(self):
        print("AuthMixin.__init__")
        super().__init__()

    def process(self):
        print("AuthMixin.process → auth check")
        super().process()


# ============================================================
# 3. CORE BUSINESS CLASS
# ============================================================

class ServiceBase(Root):
    def __init__(self):
        print("ServiceBase.__init__")
        super().__init__()

    def process(self):
        print("ServiceBase.process → core logic")


# ============================================================
# 4. FINAL CHILD (MULTIPLE INHERITANCE)
# ============================================================

class PaymentService(LoggerMixin, AuthMixin, ServiceBase):
    def __init__(self):
        print("PaymentService.__init__")
        super().__init__()

    def process(self):
        print("PaymentService.process → start")
        super().process()
        print("PaymentService.process → end")


# ============================================================
# 5. DIAMOND PROBLEM (SEPARATE MINI GRAPH)
# ============================================================

class A:
    def action(self):
        print("A.action")

class B(A):
    def action(self):
        print("B.action")
        super().action()

class C(A):
    def action(self):
        print("C.action")
        super().action()

class D(B, C):
    def action(self):
        print("D.action")
        super().action()


# ============================================================
# 6. BROKEN CLASS (ANTI-PATTERN)
# ============================================================

class BrokenAuthMixin(Root):
    def __init__(self):
        print("BrokenAuthMixin.__init__")
        Root.__init__(self)   # breaks MRO

    def process(self):
        print("BrokenAuthMixin.process")
        Root.process(self)   # bypasses chain


class BrokenService(LoggerMixin, BrokenAuthMixin, ServiceBase):
    def __init__(self):
        print("BrokenService.__init__")
        super().__init__()

    def process(self):
        print("BrokenService.process → start")
        super().process()
        print("BrokenService.process → end")


# ============================================================
# ======================= EXECUTION ==========================
# ============================================================

print("\n========== MRO (PaymentService) ==========")
print(PaymentService.mro())

print("\n========== INIT CHAIN ==========")
svc = PaymentService()

print("\n========== METHOD CHAIN ==========")
svc.process()

print("\n========== DIAMOND PROBLEM ==========")
print(D.mro())
D().action()

print("\n========== BROKEN DESIGN ==========")
broken = BrokenService()
broken.process()
