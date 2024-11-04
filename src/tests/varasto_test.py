import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_tilavuus(self):
        self.varasto = Varasto(-1.0)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_neg_saldo(self):
        self.varasto = Varasto(2, -1.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_maaraa_ei(self):
        saldo_nyt = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        saldo_jalkeen = self.varasto.saldo
        self.assertAlmostEqual(saldo_nyt,saldo_jalkeen)

    def test_mahtuuko_lisatessa(self):
        tila = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(tila+1)
        self.assertAlmostEqual(self.varasto.saldo,tila)

    def test_jos_lisatessa_ei_mahdu(self):
        mitatulee = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(mitatulee, 0.0)

    def test_jos_ei_otettavaa(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(maara, 5)

    def test_str(self):
        mitahalutaan = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}" 
        self.assertAlmostEqual(str(self.varasto),mitahalutaan)
