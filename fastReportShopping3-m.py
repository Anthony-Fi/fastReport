import csv
import json
import argparse
from pytrends.request import TrendReq
from pprint import pprint

pytrends = TrendReq()

# Create an argument parser
parser = argparse.ArgumentParser(description='Process some keywords.')

# Add an argument for keywords
parser.add_argument('--keywords', type=str, help='Comma-separated list of keywords')

# Add an argument for output
parser.add_argument('--output', choices=['terminal', 'csv'], default='terminal',
                    help='Output format (default: terminal)')

# Parse the command line arguments
args = parser.parse_args()

# Extract the list of keywords
if args.keywords:
    kw_list = args.keywords.split(',')
    print(kw_list)
else:
    print("No keywords provided.")

# set timeframe
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='froogle')

# save related queries
related_queries = pytrends.related_queries()

# Output the keywords
if args.output == 'terminal':
    pprint(related_queries)
elif args.output == 'csv':
    for term in related_queries:
        search_term = term
        print("Search Term Is =" + search_term)
        for key in related_queries[term].keys():
            top_or_rising = key
            print("Is it Top or Rising:" + top_or_rising)
            related_queries[term][key].to_csv('output/' + term + '_' + top_or_rising + '.csv', index=False)