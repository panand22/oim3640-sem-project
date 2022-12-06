# **Project Proposal**
### ***By: Pratik Anand***  

</br>

#
**1. The Big Idea**: 

What is the main idea of your project? What topics will you explore and what will you generate? What is your minimum viable product? What is a stretch goal?

The initial idea of my project is to create a dating matching algorithm and simple website that pairs up people based on various factors including similar interests. I plan to collect data from user inputted questions and public APIs with informations about the interests of users. 

Ideally, I would like to use web scraping to find out which factors result in the most effective connections. However, in the case I am not able to do that due to time constraints, I will use pre-existing pairing algorithms based on psychology research to pair up two individuals.  I also plan to test the effectiveness of these algorithms on public data (or through web scraping social media platforms) by conducting sentiment analysis.

The minimum viable product I will design is a simple website where users will be able to input their data and will be paired with another individual. Once individuals are paired, they will be shown a website page detailing the profile of their paired individual and why they were paired.

</br>


## ❗❗ Project Pivot:
#

As explained on the [Project Website](https://sites.google.com/view/oim3640-project-pratikanand/project-evolution-process?authuser=0), 
I realized this would be more front-end development rather than using Python. Therefore, I pivoted to building an app to predict user personalities based on user inputted text as well as their Twitter profile.

#
**2. Learning Goals**: 

My high-level learning goal is to become a better programmer and be apply to frameworks learned in this class to my project. 

Some of my more specific learning goals are as follows:

* Explore Matching Algorithms: I have always been interested in exploring matching algorithms, specifically as they pertain to facilitating authentic connections between two individuals. Therefore, I would like to learn more about what different factors result in most compatible connections. 

* Learning about database management: I will most likely need to learn more about databases such as sqlite3 to store information about users and be able to access them throughout the matching process. 

* Structure of Complicated Programs: I would like to learn more about how to best structure code in an efficient and developer-friendly manner when designing extended projects.

#
**3. Implementation Plan**: 

My implementation plan will evolve as I do more research. However, my current plan follows this process:

1. Gather information about user connections (perhaps through the Reddit API)
2. Write code to organize the different types of connections, based on psychological research (i.e. compatible MBTI personalities, common interests, etc.)
3. Conduct sentiment analysis to analyze the various types of connections
4. Choose several algorithms to pair up individuals. Write code for these algorithms. (Ex of Algorithm: MBTI personality type compatibility)
5. Test these algorithms on dummy data
6. Write code to collect user input and store it in a database
7. Design home webpage (through HTML) to collect user input through a survey format. Users will then be paired based on algorithms written in step 4. 
8. Create other webpages to showcase information about user profile to paired users and display why they were comaptible.

</br>

## ❗❗ Revised Implementation Plan:

#

As explained on the [Project Website](https://sites.google.com/view/oim3640-project-pratikanand/project-evolution-process?authuser=0), 
I pivoted my initial idea to building an app to predict user personalities, instead of matching users to each other. 

This affected the implementation plan of my project, resulting in the following steps:

1. Find Database of MBTI Personalities based on User Text

2. Develop Logic of Matching Algorithm using text similarity libraries

3. Develop simple front-end to collect inputted text for testing purposes

4. Collect data from Twitter Profile using Tweepy Library

   * Clean received data into readable text format. Remove common stopwords
5. Update Front-End

    * Add UI/UX elements

#

**4. Project schedule**: 

Based on my schedule, I plan to work on this project mainly during Thanksgiving Break. Nevertheless, I will conduct extensive research and planning before. 

My rough timeline is: 
* **Nov. 11 - 16**: Research Reddit API, Matching alorithms, and database systems: 
* **Nov 17 - 20** Conduct sentiment analysis to identify most effective connection types
* **Nov 21 - 23**: Write code for algorithms
* **Nov 23 - 24**: Test algorithms on dummy data
* **Nov 25 - 27**: Write code to store user info. in database
* **Nov 28 - 30**: Write front-end code
* **Dec 01 - 03**: Test program/refine program

#

**5. Collaboration plan**: 

I will be working on this project by myself and, therefore, will be doing all the work individually. 

I do plan to follow agile methodology by iteratively testing features I develop in my program. 

#
**6. Risks**: 

The biggest risk I view to the success of this program is not being able to store and access the user data properly, as my project essentially revolves around it. 

Moreover, not being able to access the Reddit API would detrimental to my project and definitely cause some disruptions in collecting data to understand how successful my matching algorithms would be.

#
**7. Additional Course Content**: 

What are some topics that we might cover in class that you think would be especially helpful for your project?

I think covering database management in more detail would be especially helpful for my project, as I would need to manage storing and accessing data extensively throughout my program. Moreover, I think learning about OOP would be useful to understand how to keep my code organized.
#