1. Introduction

For tha last decade video game instry has past long way from a nish market with a few game studious to a multi-billion global market with global software companies. Game industry revenue might reach an almost 307 billions by 2029 from 200 billions in 2022 (https://www.fortunebusinessinsights.com/video-game-market-102548#). Rapid growth is supported by the leaders in the inductry for instance Microsoft, Nintendo, Sone and etc. but also small game studious. Video game industry is very competative with the low barier to enter the market due to the simplification of game engines, availability of marketplaces, and possibility to communicate with players directly. However the biggest challenge for small companies is establishing a community around the game on the early stage, since there is no common place for it. Game platforms are mostly focused on AAA titles from big companies since they are generating the biggest traffic of players to them. Small developers become lost and forgoten in the sadow from the big labels. Therefore, this project aims to solve this issue and provide platform for small game developers to publish their works and build community of fans around them.

Small indie game studious do not have place where they can easily test and get feedback about the game from players on the pre-release stage. Since they have limited scale and budget need to start increasing their exposure early in the game development process to build a potential player base or to receive feedback and assistance from external sources. Currently, their options are mainly limited to setting up their own blogs or posting updates on personal social media platforms. Therefore, the platform we plan to develop aims to integrate these resources for indie games in development, allowing potential players to access information they care about in one place and helping developers address issues encountered during development, so they are no longer isolated and unsupported.

A platform creation is a challanging project since balance of interests between developers and players should persist. The ain is to make the platform easy to use for both player and developer, and intuitive for browsing and interacting with. Therefore, the platform creation requires to store a content of developers and players, build packages for several interfaces, integrate an AI-generated analysis reports.

Bisides the technical challenges, the project has significant benefits for users. Game studious will be able to upload test builds, publish promotional videos, triger event notifications, distribute digital materials (such as character designs and soundtracks), get a feedback about the game on pre-released stage, and receive AI-generated analysis reports with a fan's community opinion. Players will be able to track the development progress of games they are interested in, participate in ratings and reviews, receive invitations for game testing.

2. Related Work

Although some well-known game distribution platforms like Steam and GOG do provide platforms for the release and promotion of indie games, these platforms focus more on promoting completed works or stage-complete early-access products and facilitating community interaction. Due to the large number of commercial rockstar AAA games on these platforms, the attention and support for indie games are often insufficient. In this situation, many game developers choose to use official social media account to promote their games like on Instagram/Discord, but a player targeting is a weak point, since a social media platforms are not specialize on this segment. Moreover, the biggest challenge is in case of cooperation with players, game developers has to send direct personal invitation to the players to gather their feedback, analyze it, and incorporate changes after. Or skipping this development part with public tests and release game without it. This decrease a chance for game to be successefull at the end.   

Therefore, creation of a place where small games studious and players can meet each other and share their ideas, discuss some features and interact with each other is required. 
the players will familiarize themselves with the pre-released indie game info, interact with developers, and contribute to the work-in-process projects. Developers will be able to focus on games development, without spreading resourses on gathering the players from various platforms. The platform will be able to provide a one-stop service for developers to upload game test builds and interact with potential players.

3. Approach

**How will you solve the problem? **

The initial project is a platform (web application) where game developers can share their games in the development stage for testing/feedback gathering. 


This web application will primarily serve independent game developers or small indie game studios. Main focus is on facilitating early-stage game development content.
  Independent game developers will be able to create a homepage for their games. On this page, developers can post descriptions of the game, patch notes, playtest events, trailers, and more. Developers with needs can upload stage-specific game test builds for player testing, and quickly receive ratings and feedback from interested players about that stage's results, thus improving the final product more effectively. The platform would allow developers to post crowdfunding initiatives or raise funds by promoting (while this is not a project feature to facilitate it)
  Players would have a chance to familiarize themselves and test games before game release. They would be able to browse and track the development progress of games they are interested in, participate in testing, and directly contact developers through the platform to leave suggestions that help improve the game.
 The platform will provide a summary of the games based on the players feedback by gathering them and summarizing it via AI in a short article for each game. That helps players to have a brief overview of the game. And also it gives game developers a summary of feedbacks.



Our project should create a platform where game developers can share their early-stage games for testing/ feedback gathering. Players would have a chance to familiarize themselves and test games before game release. Platform also will provide summary about the game based on players feedback by gathering them and summarizing via AI in a short article. That helps players to have short overview and also game developers get summary of feedbacks.

Guo: As an additional note to the above, this web application will primarily serve independent game developers or small indie game studios. It aims to integrate scattered indie game resources while providing a platform for developers with limited budgets and scales to connect with potential players during the game development process. Independent game developers will be able to create a homepage for their games in development. On this page, developers can post descriptions of the game, patch notes, playtest events, trailers, and more. Developers with needs can upload stage-specific game test builds for player testing, and quickly receive ratings and feedback from interested players about that stage's results, thus improving the final product more effectively. Players can browse and track the development progress of games they are interested in, participate in testing, and directly contact developers through the platform to leave suggestions that help improve the game.

JingChen: Platform focus on facilitating early stage and Indie game development. The platform could help developer crowdfunding or raise fund by promoting.






We going to create website. To give possibility to Studious register an account, publish their materials, games news, announcements. Players can register their accounts, leave a comment about the games on the website. AI will collect comments and create short summary for players and game studious.

**What product will you be building? **

The Website as a front-end interface and database (game studious and players accounts). Additionally, we will use AI API to summarize feedback for players and game studious.

**What is the software architecture?**

Guo：We currently plan to adopt an architecture similar to MVC for building our platform.

**What are the algorithms involved? **

Create constructors for new accounts, comments, posts. Sort, store, transfer data from website to database and back.

Guo: it might be involving some search algorithms like searching based on keywords and filter search results on given fields like game genre or developers.

**How will you be implementing it? **

We will create the Website for the game studious and players. Gather their information in database and publish it on the website.
 
**What hardware will you use and why? **

We will use only cloud services for this project since we don’t have any common infrastructure to develop and deploy our project.

**What operating system will you use and why? **

It is web development therefore website should be OS neutral.

JingChen: Mac OS, Windows 10 (Linux) As the all teammates are familiar with Mac OS and Windows, and most required development tools has been installed.
Ubuntu:User friendly, large community, Support for multiple development tools


**What programming language will you use and why? **

Need to choose what we going to use for website building Python (Django and Flask) or JavaScript (React) – it is the most popular programming languages in web development
Database: MySQL or SQLite ---- SQL is the standard for database management

Guo: For the framework, currently we are evaluating between Django and ASP.net
JingChen: HTML for website layout CSS for styling .js for interaction C# or java for backend SQL for database 

**What libraries will you use and why? **

Depends from the language and database we choose.

JingChen:
BootStrap:for webpage template, 
React.js: interactive UI
Me and Guo developed a ready-to-ues ASP.NET based CRUD template last term which could be very useful for the website realization.
Django(Python) and Spring Boot(Java) could be optional.


4. Deliverables

**State the deliverables (documents, features implemented in code, etc.) for EACH week. **

We going to prepare various diagrams (use case, class, state, sequence diagrams) and database architecture (tables) to split the particular tasks during development (ensure that we are on the one page in terms of necessary steps to be done)

JingChen:
1.WebApp source code, 
2.usage and maintaining instruction, 
3.Web link deployed on git or other platforms.


5. Evaluation

**How will you define success? E.g., accuracy, speed, ease of use, user adoption, user ratings. **

We will use auto-test for the website to test functionality and also user feedback for usability.

Guo：Core functionalities need to be implemented without errors; the user interface should be simple and aesthetically pleasing, making it easy for new users to get started and for experienced users to navigate quickly.


**How will you measure success? E.g., case studies, benchmarking. **

Firstly, all features should work without errors. Secondly, website should be intuitive and user friendly. 

Guo：Before syncing each version to the main branch on GitHub, we will conduct local testing to ensure that the core functionalities run smoothly and to define and test various exceptions. After syncing, we will perform additional manual testing to ensure the stability of the current version.

1. Game Browsing and Discovery
Benchmark 1: Game Search Functionality
•	Metric: Game search results should be relevant, accurate, timely.
Benchmark 1.2: Game Filtering and Sorting
•	Metric: Filters should be applied instantly, and sorting should correctly rank games by criteria such as popularity, release date, or rating.

2. Game Uploading for Developers
Benchmark 2.1: Game Upload Time
•	Metric: Games should be uploaded within a reasonable time frame 
Benchmark 2.2: Game Metadata Submission
•	Metric: Developers should be able to upload metadata (game title, description, screenshots, etc.) within 1 minute without errors.



6. Risks 

**What can go wrong? **

Volume of work might exceed our capabilities (time, skills, experience)
Guo:  switch to Django might cause high learning curve because we don’t have much experience with this framework before; The storage solution for the website(for developers to upload videos and  compressed files) might also be a potential issue because we don’t have experience on such large scaled storage solutions previously and it might requires paid cloud storage plan.

**What will you do to minimize the chances of things going wrong? **

We invest time in documentation aspect. To have clear plan what we need to do and how we going to implement it. It should give us clear pace to complete the project. 

Guo:  We are still evaluating the framework we will choose. If we decide on Django, we will first create a quick prototype to validate the feasibility of the process. Regarding the storage solution, we might not to handle storage on our own website. Instead, we may require developers to upload their own cloud storage links and video platform links. 


**What will you do if things still go wrong? **

We going to have regular and close interaction during the full length of the project. (regular meetings and on-hoc calls)

Guo: and we will have alternative plans which might be easier on technique aspect such as the storage plan above.

7. Conclusion

Summarize the report. 
(Most of function will be used in this web application are very identical to me and Guo’s previous project, the current idea realization and project development could be quiet feasible.) 

8. References

