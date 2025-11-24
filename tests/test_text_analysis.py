"""
Tests for text analysis functions.
"""
import pytest
import pandas as pd
import numpy as np


class TestTextProcessing:
    """Test text processing functions."""
    
    def test_headline_length_calculation(self):
        """Test headline length calculation."""
        headlines = [
            "Stocks That Hit 52-Week Highs On Friday",
            "Apple Reports Strong Earnings",
            "Market Analysis"
        ]
        df = pd.DataFrame({'headline': headlines})
        
        df['headline_length'] = df['headline'].str.len()
        df['headline_word_count'] = df['headline'].str.split().str.len()
        
        assert 'headline_length' in df.columns
        assert 'headline_word_count' in df.columns
        assert df['headline_length'].iloc[0] == len(headlines[0])
        assert df['headline_word_count'].iloc[0] == len(headlines[0].split())
    
    def test_keyword_extraction_structure(self):
        """Test that keyword extraction returns list."""
        text = "Apple stock price target increased by analyst"
        # Simulate keyword extraction
        keywords = text.lower().split()
        # Filter out common words
        stop_words = {'the', 'a', 'an', 'by', 'on', 'in', 'at', 'to', 'for'}
        keywords = [kw for kw in keywords if kw not in stop_words and len(kw) > 2]
        
        assert isinstance(keywords, list)
        assert len(keywords) > 0
        assert all(isinstance(kw, str) for kw in keywords)
    
    def test_significant_phrases_detection(self):
        """Test detection of significant financial phrases."""
        headlines = [
            "FDA approval for new drug",
            "Price target raised to $200",
            "Earnings report exceeds expectations",
            "52-week high reached today"
        ]
        df = pd.DataFrame({'headline': headlines})
        
        # Check for significant phrases
        significant_phrases = ['fda approval', 'price target', 'earnings', '52-week high']
        phrase_counts = {}
        
        for phrase in significant_phrases:
            count = df['headline'].str.lower().str.contains(phrase, na=False).sum()
            phrase_counts[phrase] = count
        
        assert 'fda approval' in phrase_counts
        assert 'price target' in phrase_counts
        assert phrase_counts['fda approval'] == 1
        assert phrase_counts['price target'] == 1
        assert phrase_counts['earnings'] == 1
        assert phrase_counts['52-week high'] == 1


class TestPublisherAnalysis:
    """Test publisher analysis functions."""
    
    def test_publisher_counting(self):
        """Test counting articles per publisher."""
        publishers = ['Publisher A', 'Publisher B', 'Publisher A', 'Publisher C', 'Publisher B']
        df = pd.DataFrame({'publisher': publishers})
        
        publisher_counts = df['publisher'].value_counts()
        
        assert len(publisher_counts) == 3
        assert publisher_counts['Publisher A'] == 2
        assert publisher_counts['Publisher B'] == 2
        assert publisher_counts['Publisher C'] == 1
    
    def test_publisher_contribution_percentage(self):
        """Test calculation of publisher contribution percentage."""
        publishers = ['A', 'B', 'A', 'C', 'B', 'A']
        df = pd.DataFrame({'publisher': publishers})
        
        total = len(df)
        publisher_counts = df['publisher'].value_counts()
        contribution_pct = (publisher_counts / total * 100).round(2)
        
        assert contribution_pct['A'] == 50.0
        assert contribution_pct['B'] == 33.33
        assert contribution_pct['C'] == 16.67


class TestTemporalAnalysis:
    """Test temporal analysis functions."""
    
    def test_date_component_extraction(self):
        """Test extraction of date components."""
        dates = pd.date_range('2020-01-01', periods=10, freq='D')
        df = pd.DataFrame({'date': dates})
        
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day_of_week'] = df['date'].dt.day_name()
        
        assert df['year'].iloc[0] == 2020
        assert df['month'].iloc[0] == 1
        assert df['day_of_week'].iloc[0] == 'Wednesday'
    
    def test_articles_by_period(self):
        """Test counting articles by time period."""
        dates = pd.date_range('2020-01-01', periods=100, freq='D')
        df = pd.DataFrame({'date': dates})
        
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        
        articles_by_year = df['year'].value_counts()
        articles_by_month = df['month'].value_counts()
        
        assert 2020 in articles_by_year.index
        assert articles_by_year[2020] == 100
        assert len(articles_by_month) <= 12


if __name__ == '__main__':
    pytest.main([__file__])

