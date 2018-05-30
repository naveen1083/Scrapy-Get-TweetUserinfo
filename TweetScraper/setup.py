setup(    
  name='TweetScraper',
  version='1.0',    
  packages=find_packages(),    
  package_data={        'TweetScraper': ['resources/*.txt']    },
  entry_points={        'scrapy': ['settings = TweetScraper.settings']    },
  zip_safe=False, )
