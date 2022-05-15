import unittest
import hw3


class TestAmpliconFinder(unittest.TestCase):
    def test_extend_ambiguous_seq(self):
        expected = ['ACC', 'ACG', 'ACT', 'AGC', 'AGG', 'AGT']
        actual = hw3.extend_ambiguous_seq('ASB')
        self.assertListEqual(actual, expected)

    def test_reverse_modifier(self):
        expected = ['GGT', 'CGT', 'AGT', 'GCT', 'CCT', 'ACT']
        actual = hw3.reverse_modifier(['ACC', 'ACG', 'ACT', 'AGC', 'AGG', 'AGT'])
        self.assertListEqual(actual, expected)

    def test_create_re_primer(self):
        expected = ['ATCCAT.+TTGGT', 'ATCCAT.+TTCGT', 'ATCCAT.+TTAGT', 'ATCCAT.+TTGCT', 'ATCCAT.+TTCCT', 'ATCCAT.+TTACT']
        actual = hw3.create_re_primer(['ATCCAT'], ['TTGGT', 'TTCGT', 'TTAGT', 'TTGCT', 'TTCCT', 'TTACT'])
        self.assertListEqual(actual, expected)

    def test_amplicon_search(self):
        expected = []
        list_primers = ['ATCCAT.+TTGGT', 'ATCCAT.+TTCGT', 'ATCCAT.+TTAGT', 'ATCCAT.+TTGCT', 'ATCCAT.+TTCCT', 'ATCCAT.+TTACT']
        #actual = hw3.amplicon_search(hw3.SeqIO.parse('./test_data/hw3_seq.fasta', 'fasta'), list_primers)
        actual = hw3.amplicon_search(open('./test_data/test_hw3.fasta'), list_primers)
        self.assertListEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()