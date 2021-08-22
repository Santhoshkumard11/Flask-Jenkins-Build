import unittest

from snippet import check_posted_data

class TestSnippet(unittest.TestCase):
    
    def test_check_posted_data_first(self):
        print(f"Testing function - {check_posted_data.__name__}")
        
        data_list = [[{"x": 184,"y": 323},"add",200], [{"x": 143,"y": 0},"division",302]
                     , [{"x": 143},"division",301]]
        
        for data in data_list:
            
            result = check_posted_data(data[0],data[1])
            
            self.assertEqual(result, data[2])

