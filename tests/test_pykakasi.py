# -*- coding: utf-8 -*-
import unittest
import pykakasi

class TestPyKakasi(unittest.TestCase):

    def test_kakasi_hepburn(self):

        TESTS = [
            (u"構成",         "Kousei"),
            (u"好き",         "Suki"),
            (u"大きい",       "Ookii"),
            (u"かんたん",     "kantan"),
            (u"にゃ",         "nya"),
            (u"っき",         "kki"),
            (u"っふぁ",       "ffa"),
            (u"漢字とひらがな交じり文", "Kanji tohiragana Majiri Bun"),
            (u"Alphabet 123 and 漢字", "Alphabet 123 and Kanji"),
            (u"日経新聞", "Nikkeishinbun"),
            (u"日本国民は、","Nihonkokumin ha,")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a")
        kakasi.setMode("K","a")
        kakasi.setMode("J","a")
        kakasi.setMode("r","Hepburn")
        kakasi.setMode("s", True)
        kakasi.setMode("E","a")
        kakasi.setMode("a",None)
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_kunrei(self):

        TESTS = [
            (u"構成",         "Kousei"),
            (u"好き",          "Suki"),
            (u"大きい",       "Ookii"),
            (u"かんたん",     "kantan"),
            (u"にゃ",          "nya"),
            (u"っき",           "kki"),
            (u"っふぁ",        "ffa"),
            (u"漢字とひらがな交じり文", "Kanzi tohiragana Maziri Bun"),
            (u"Alphabet 123 and 漢字", "Alphabet 123 and Kanzi"),
            (u"日経新聞",     "Nikkeisinbun"),
            (u"日本国民は、", "Nihonkokumin ha,")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a")
        kakasi.setMode("K","a")
        kakasi.setMode("J","a")
        kakasi.setMode("r","Kunrei")
        kakasi.setMode("E","a")
        kakasi.setMode("a",None)
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_J2H(self):

        TESTS = [
            (u"構成",         u"こうせい"),
            (u"好き",         u"すき"),
            (u"大きい",       u"おおきい"),
            (u"かんたん",     u"かんたん"),
            (u"にゃ",         u"にゃ"),
            (u"っき",         u"っき"),
            (u"っふぁ",       u"っふぁ"),
            (u"漢字とひらがな交じり文", u"かんじとひらがなまじりぶん"),
            (u"Alphabet 123 and 漢字", u"Alphabet 123 and かんじ"),
            (u"日経新聞",     u"にっけいしんぶん"),
            (u"日本国民は、", u"にほんこくみんは、")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H",None)
        kakasi.setMode("K",None)
        kakasi.setMode("J","H")
        kakasi.setMode("s",False)
        kakasi.setMode("C",True)
        kakasi.setMode("E",None)
        kakasi.setMode("a",None)
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_H2K(self):

        TESTS = [
            (u"かんたん",     u"カンタン"),
            (u"にゃ",         u"ニャ")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","K")
        kakasi.setMode("S"," ")
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_K2H(self):

        TESTS = [
            (u"カンタン",u"かんたん"),
            (u"ニャ",    u"にゃ")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("K","H")
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)
 
    def test_wakati(self):
        TESTS = [
        (u"交じり文", u"交じり 文"),
        (u"ひらがな交じり文", u"ひらがな 交じり 文"),
        (u"漢字とひらがな交じり文", u"漢字 とひらがな 交じり 文")
        ]
        wakati = pykakasi.wakati()
        converter = wakati.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)

    def test_kakasi_a2E(self):

        TESTS = [
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"),
            ("abcdefghijklmnopqrstuvwxyz",
             u"ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"),
            ("!\"#$%&'()*+,-./_ {|}~",
             u"！＂＃＄％＆＇（）＊＋，－．／＿　｛｜｝～")
        ]

        kakasi = pykakasi.kakasi()
        kakasi.setMode("a","E")
        converter  = kakasi.getConverter()
        for case, result in TESTS:
            self.assertEqual(converter.do(case), result)
