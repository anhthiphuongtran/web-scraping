#**SCRAPING DATA FROM TIKI WEBSITE USING PYTHON**
 

## About
*This project is about data scraping using Python. In this project, I use Beautiful Soup library to pull out the price of "Story Telling with Data" - one of the most famous books for data analysis sold on [Tiki website](https://tiki.vn/storytelling-with-data-ke-chuyen-thong-qua-du-lieu-cuon-cam-nang-huong-dan-truc-quan-hoa-du-lieu-p76013378.html?spid=76013379) 


![pic06](https://github.com/anhthiphuongtran/web-scraping/assets/105230494/42d72614-bd31-4a30-af95-0c7a4346ed45)

* While the website continuously updates the book's price, I will write code to extract the price and automatically send an email to myself (using smtplib) notifying when the price is below my cut-off price, or in other words, the price I am willing to pay.

## Dependencies:

1. Python v3.x is required.
2. Beautiful Soup library is required to scape web data.
3. Smtp module is required to send email automatically within the program.

## Additional information
The code can be uploaded on [Python Anywhere](https://www.pythonanywhere.com/) so that the program can be run in the cloud to continuously check the price and send email automatically even if I do not turn on my computer.

