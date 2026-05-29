import unittest
import risk_classifier as rc


def row(**kw):
    base = {
        "system_id": "T", "system_name": "T", "owner": "T", "use_case_category": "",
        "annex_iii_area": "", "annex_i_product": "no", "transparency_obligation": "no",
        "gpai_model": "no", "provider_or_deployer": "provider", "prohibited_practice": "no",
        "exclusion_narrow_task": "no", "exclusion_human_result": "no",
        "exclusion_no_individual": "no", "exclusion_preparatory": "no",
    }
    base.update(kw)
    return base


class TestClassify(unittest.TestCase):
    def test_explicit_prohibited(self):
        self.assertEqual(rc.classify_system(row(prohibited_practice="yes"))["tier"], "UNACCEPTABLE")

    def test_keyword_prohibited_warns(self):
        r = rc.classify_system(row(use_case_category="social scoring of citizens"))
        self.assertEqual(r["tier"], "UNACCEPTABLE")
        self.assertTrue(r["warnings"])

    def test_annex_i_high(self):
        self.assertEqual(rc.classify_system(row(annex_i_product="yes"))["tier"], "HIGH")

    def test_annex_iii_high(self):
        self.assertEqual(rc.classify_system(row(annex_iii_area="4"))["tier"], "HIGH")

    def test_art_6_3_exclusion_downgrades(self):
        r = rc.classify_system(row(annex_iii_area="4", exclusion_narrow_task="yes"))
        self.assertNotEqual(r["tier"], "HIGH")
        self.assertTrue(r["exclusion"])

    def test_limited_gpai(self):
        self.assertEqual(rc.classify_system(row(gpai_model="yes"))["tier"], "LIMITED")

    def test_limited_transparency(self):
        self.assertEqual(rc.classify_system(row(transparency_obligation="yes"))["tier"], "LIMITED")

    def test_minimal(self):
        self.assertEqual(rc.classify_system(row())["tier"], "MINIMAL")

    def test_validate_bad_area(self):
        issues = rc.validate_row(row(annex_iii_area="9"))
        self.assertTrue(any("annex_iii_area" in i for i in issues))

    def test_validate_bad_yesno(self):
        issues = rc.validate_row(row(gpai_model="maybe"))
        self.assertTrue(any("gpai_model" in i for i in issues))


if __name__ == "__main__":
    unittest.main()
