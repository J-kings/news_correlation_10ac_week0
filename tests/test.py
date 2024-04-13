import pandas as pd
import unittest

# Load the DataFrame from 'rating.csv' 
rating = pd.read_csv('././rating.csv')

# Adding the content_length and title_word_count columns to the DataFrame
rating['content_length'] = rating['content'].str.len()
rating['title_word_count'] = rating['title'].str.split().str.len()

class TestContentAndTitleLength(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Use the 'rating' DataFrame directly
        cls.data = rating
    
    def test_content_length_calculation(self):
        # Assuming the content_length calculation is correct, this test will pass if the DataFrame is correctly loaded and calculated
        # This is a basic test to check if the 'content_length' column exists and has the correct type
        self.assertTrue('content_length' in self.data.columns, "The 'content_length' column does not exist.")
        self.assertTrue(pd.api.types.is_integer_dtype(self.data['content_length']), "The 'content_length' column is not of integer type.")
        
    def test_title_word_count_calculation(self):
        # Similar to the content_length test, this checks the existence and type of the 'title_word_count' column
        self.assertTrue('title_word_count' in self.data.columns, "The 'title_word_count' column does not exist.")
        self.assertTrue(pd.api.types.is_integer_dtype(self.data['title_word_count']), "The 'title_word_count' column is not of integer type.")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
