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

The initial project is a platform (web application) where game developers can share their games in the development stage for testing/feedback gathering. 
This web application will primarily serve independent game developers or small indie game studios. Main focus is on facilitating early-stage game development content.
Independent game developers will be able to create a homepage for their games. On this page, developers can post descriptions of the game, patch notes, playtest events, trailers, and more. Developers with needs can upload stage-specific game test builds for player testing, and quickly receive ratings and feedback from interested players about that stage's results, thus improving the final product more effectively.
Players would have a chance to familiarize themselves and test games before game release. They would be able to browse and track the development progress of games they are interested in, participate in testing, and directly contact developers through the platform to leave suggestions that help improve the game.
The platform will provide a summary of the games based on the players feedback by gathering them and summarizing it via AI in a short article for each game. That helps players to have a brief overview of the game. And also it gives game developers a summary of feedbacks.

The project aims to adopt an architecture similar to MVC (Model View Controller) for building a platform. It's a software design pattern commonly used in web development by devideing interface by 3 interconnected elements. According to Figure 1 (Use Case Diagram), it is planned to have 2 interfaces for Game Developers and Players. Additionally, it is planned to use one of the AI's API to process a Players input (ratings and comments) to generate data insights. To execute this archetecture are developed a Class Diagram illustrated as Figure 2 (Class Diagram). Main actors will have their own entites with related methods. Furtehrmore, the project will include Database archetecture represented in Figure 3 (Database Architecture). Algorithms might be involving some search algorithms like searching based on keywords and filter search results on given fields like game genre or developers. 

The project will be performend with the following Software stack:
The Framework will be implimented with Django Web Framework since is a free and open-source, Python-based web framework that runs on a web server. It fully supports project MVC architecture concept. Additionally, it is tailored to use relational database which is planned to use.   
Front-End will include BootStrap to manage a web application to impliment a website HTML and CSS programming languages. To enchance a web apllication usability the front-end will include React.js that uses JavaScrip language for styling websites.  
For the Back-Edn project will use a Python as a major programming language with support of SQL to communicate with Database. A Database will be implemented in MySQL to store the data as an relational database. Additionally, the project will include externatl APIs to interact with AI to process data. 

4. Deliverables

The project includes the following diagrams: use case, class(entites), state, sequence diagrams. The database architecture consist of tables and access matrix to manage the data.
Major mielstones are Midterm Demo version submission and Final project submission. Meantime, the deliverables inlude also other interim milestones. For the project execution task and deliverables plan to be distributed on the weekly team meeting. 

Sep 4 | Week 1 | Project idea generation 
Sep 11 | Week 2 | Project concept developing
Sep 18 | Week 3 | Preparation of Documentation 
Sep 25 | Week 4 | Establishment of Enviroment, Framework, Database and Development Tools
Oct 2 | Week 5 | Creation of main Entities, Methods, Database Tables
Oct 9 | Week 6 | Simple front-end concept preparation
Oct 16 | Week 7 | Demo version demonstartion and Mid-term-report submission
Oct 23 | Week 9 | Development of non-essential features of the project
Oct 30 | Week 10 | Enchance front-end development
Nov 6 | Week 11 | Testing and debugging
Nov 13 | Week 12 | Testing and debugging
Nov 20 | Week 13 | Preparation of presentation and the final report
Nov 27 | Week 14 | Presentation and final report submission

To communicate and maintaine efficient project execution the project team plan to keep daily contact in established communication channels in messengers, GITHub and other resources.   

5. Evaluation

Evaluation of deliverabled tasks is planned to perform by conductiong weekly cross team discussion and presentation of functionality. Additionally, it is planned to have a 2 weeks of testing and debugging to achive high quality product at the end of the project. To achive this the team plan to develop and perform auto-test for the web application in order to test functionality. Additionally, the team plan to make user testing gather feedback about usability and user product satisfaction. It is planned to assess the core web application functionalities for non-error conditions. And also the user interface should be simple and aesthetically pleasing, making it easy for new users to get started and for experienced users to navigate quickly.

As a bechmark for evaluation the product has to follow those stadards:  

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

The project major risks are the diss-sichronisation within the teamm, complexity of software stack, and size of the project. To mitigate those risks the team plan to implement following measures:
- The team plan to develope documentation. In order to have clear plan what is the scope of the project and how it is going to be delivered. This approach aims to provide clear project structure with the ability to nominate a specific tasks to ech team member and set deadline for delivery.
- Risk of stack complexity is planned to be mitigated by team members expirience in various topics. Team has an expirience in web development and database maintenance. All are familiar with Python programming language and knowlange in front-end syntacys. Also team have a hands on expirience with SQL in Databases.
- Size of the proect is also an risk for the project completion, but mitigation measure is to outline the project scope in details before the kickoff and to be flexible during the project to adjust and allocate team resources in required direction. 
The team is going to have regular and close interaction during the full length of the project to be able to deliver the project in time and in accordance with high standards in softaware industry. 

7. Conclusion

Summarize the report. 
(Most of function will be used in this web application are very identical to me and Guo’s previous project, the current idea realization and project development could be quiet feasible.) 

8. References

