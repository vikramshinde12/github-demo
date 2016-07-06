from NewsSearch import searchword
import unittest

class TestSearchWord(unittest.TestCase):
    def test_query1(self):
        self.assertEqual(searchword('HSCIC_News.txt', 'Care Quality Commission', 'OR'), [0, 1, 2, 3, 4, 5, 6])

    def test_query2(self):
        self.assertEqual(searchword('HSCIC_News.txt', 'September 2004', 'OR'), [9])

    def test_query3(self):
        self.assertEqual(searchword('HSCIC_News.txt', 'general population generally', 'OR'), [6,8])

    def test_query4(self):
        self.assertEqual(searchword('HSCIC_News.txt', 'Care Quality Commission admission', 'AND'), [1])

    def test_query5(self):
        self.assertEqual(searchword('HSCIC_News.txt', 'general population Alzheimer', 'AND'), [6])

    def test_query6(self):
        self.assertEqual(searchword('HSCIC_News.txt', 'ABCD', 'OR'), [])

    def test_nullTypeOfSearch(self):
        self.assertEqual(searchword('HSCIC_News.txt', 'general population Alzheimer', 'XX'), 'Please enter correct Type of Search')

    def test_fileNotFound(self):
        self.assertRaises(FileNotFoundError,searchword, 'HSCIC_Breaking_News.txt', 'September 2004', 'AND')

    def test_nullFileName(self):
        self.assertRaises(FileNotFoundError, searchword, '', 'September 2004', 'AND')

    def test_spaceInSearchWords(self):
        self.assertEqual(searchword('HSCIC_News.txt', '  general     population Alzheimer   ', 'AND'), [6])

    def test_Path(self):
        self.assertEqual(searchword('C:/Users/vikramps/Documents/Big Data/Test1/News2.txt', 'Responsible interactive charts highlight', 'AND'), [11])

    def test_lowercase(self):
        self.assertEqual(searchword('hscic_news.txt', 'general population alzheimer', 'and'), [6])

    def test_uppercare(self):
        self.assertEqual(searchword('HSCIC_NEWS.TXT', 'GENERAL POPULATION ALZHEIMER', 'AND'), [6])

if __name__ == '__main__':
    unittest.main(exit=False)