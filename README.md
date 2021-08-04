Running the application:  This little application is running live --
simply type the external IP '18.215.124.12' into your browser.  Usernames
may be anything of your choosing (nothing is authenticated), and >2 users
may participate in the chat from different browsers/machines.  The app was 
containerized using Docker, and is running on an EC2 instance on AWS with 
a DynamoDB back-end.  As it stands, I'm running it on a single t2.micro 
instance, which is cheap.  If I were building something to a larger scale, 
I'd use something a little more robust that a t2.micro and use multiple 
instances across different geographic regions for greater performance and 
availability.

The code: as an exercise, I wanted to build something specific to Guild's 
tech stack; I understand that Guild uses some Python (and may be using it 
more in the near future), along with AWS.  I'd had some cursory exposure 
to the Python/Flask framework during my schooling, and that seemed like a 
great tool for this little chat app; building URLs is intuitive, you can do
lots with a little bit of code, and the problem didn't require a bunch of DOM
manipulation that might've been easier with something like JavaScript.

A quick note about unit tests: I'm a big TDD fan, but I have much more
experience writing and testing command-line applications than full-stack
apps.  I attempted to get some tests up and running for this, which would
have included mocking a database, testing response codes, etc; however, I 
already had a few more hours into this than intended, and decided to dedicate
my efforts more toward refreshing my knowledge of Flask and AWS.  I look forward 
to learning more about testing Flask applications outside the scope of this 
project.

Known bugs: 
- A user must refresh their page or submit a new message in order for the chat
screen to refresh with all the latest database entries.  I'm fairly certain 
this could be rectified with an amended ajax call (see the /static/application.js
file).  The function, in its current form, repeats every three seconds as intended
for the purpose of refreshing the chat screen, but I don't seem to be making the 
request to the database correctly.  (I look forward to working with other engineers 
who can help fill in my knowledge gaps when it comes to async requests.)
- Python's datetime.today() method (rather, my use of it thereof) seems to be 
returning somewhat unpredictable time data that impacts the proper sorting of 
chat messages.  This only seems to occur when posting a new message several hours
after the previously posted message, and may not be noticed in your review.
- As mentioned above, my experience lies more in backend code, though I'm writing
more and more front-end code in my personal projects each day.  As such, please
forgive my faulty element positioning as it relates to responsiveness at different
screen sizes.  I'll learn.  :)

Performance considerations: this is a toy application with a database to match.
As such, my Flask application loops through and prints the database entries each
time index.html reloads.  At scale, this would be an expensive operation.  I can
think of several ways in which this might be rectified.  First, the database could
be queried only for entries that fall after a certain datetime, thus limiting the
number of entries written to the chat window (think Slack's free tier, which only 
displays messages from the last several weeks).  Secondly, I have a feeling my ajax
function could be amended to get only new entries, then write them to the DOM
as list items.  Async requests, again, represent a hole in my knowledge that I look
forward to learning more about.