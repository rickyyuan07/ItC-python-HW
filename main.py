from crawler import Crawler
from args import get_args
from datetime import datetime
import csv

if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    content = crawler.crawl(args.start_date, args.end_date)
    # TODO: write content to file according to spec
    with open(args.output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(content)):
            writer.writerow([datetime.strftime(content[i][0], "%Y-%m-%d")
, content[i][1], content[i][2]])
