--------SOLUTIONS BY ARCHITH SARMA---------------------------------------




I chose the following problem statements and have solved three questions, just in case if any problem is solved only partially

Problem Statement 4
__________________
Given a video (any popular movie) or audio file (popular music), write a subtitle/lyrics finder program for them using any third-party API. 
Input: Audio/Video File path (Hint: You can use the name of the file, the hash or Acoustic ID for query)
Output: Download link to the subtitle/lyrics or The File Itself
Partial Acceptable Solution: To find it using name of the file only
Complete solution: Path or Download URL to the caption. (You can Solve for Either Video or Audio, or both it's up to you)

Solution - The program searches the lyrics on the website "https://songsear.ch" based on the input song name/filename in the searchbar(its xpath is used) and then prints the url where the lyrics are available for that song. The user has to select which song lyrics to download, as there can be multiple songs with the same name. Screenshot is attached-Screenshot 129 corresponds to problem 4.


Problem Statement 8
__________________
Write a browser automation script (e.g., using Selenium, puppeteer, phantomjs, or any other method known to you) to take a URL as an input for an HTML Input Form (for any random website) and then fill it automatically according to the fields. For e.g., if one of the fields in the form is asking for First Name, then you must fill with a first name.  
Example URL for HTML Input Form:
http://bit.ly/2sAoSa6
http://www.canwinconsulting.com/contact.html
https://www.bookchor.com/Contact
https://ebookpdf.biz/contact-us/
https://www.targetpublications.org/contacts/

Solution- The selenium script autofils the form" https://docs.google.com/forms/d/e/1FAIpQLSf-FsUy0wzGdqpYCECZK5SNdGNMuY-dRGlLq96PlUkKoc3RHQ/viewform?embedded=true" (given in the question). Using the xpath to each input field, the form is filled with the hardcorded inputs. Screenshot is attached-Screenshot 128 corresponds to problem 8.





Problem Statement 9
__________________
Write a program to read and search a given (your) email (with email and password provided to the program) for 5 recent congratulations emails you received.
Input: Email Username, Password, Email: Configuration (Can hardcode in the program)
Output: Subject of 5 Mails
Partial Acceptable Solution: Get last five emails
Complete solution: Get the last five emails containing words similar or equivalent to "congratulation."
Note: You can remove your email and password before submitting and instruct us in the text file to let us put our own email/password to test your code.



Solution- The selenium script inputs the username and password, logins into an individual's gmail account using xpath (username and password is hardcoded into the script). Now, it finds the searchbar through the xpath, searches for 'congratulations' and hits the search button. Hence, all the recent emails matching will be displayed.
Note-- Some chrome versions and other browsers don't allow automated login and will display "browser or app may not be secure."
