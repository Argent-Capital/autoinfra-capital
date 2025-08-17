from app.services.financials import npv, irr

def test_npv():
    assert round(npv(0.1, [-100, 60, 60, 60]), 2) == 44.15

def test_irr_basic():
    val = irr([-100, 60, 60, 60])
    assert 0.3 < val < 0.4
