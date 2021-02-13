
dialogues = {}
dialogues['reject'] = 'Someother time'
dialogues['GREET1'] = {}

dialogues['GREET1']['text1'] = '<b>MESSAGE FROM KOWSHIK:</b>\nHi there, I am Kowshik Chilamkurthy. Thanks for taking out your valuable time and for messaging my personal agent/bot. My buddybot will help you understand about my professional journey and my general outlook towards life.'
dialogues['GREET1']['text2'] = 'Now I will let my buddybot take over this conversation.\nNOTE: My buddybot can be excessively humorous sometimes! Do you still want to continue talking to my BuddyBoy'
dialogues['GREET1']['options'] =[['Yes, Ofcourse'], ['No, Some other time']]
dialogues['BYE'] = 'Thanks for your wonderful time, Do ping me for any more questions about kowshik and mail kowshik @kowshikchilamkurthy@gmail.com for any queries.' 
dialogues['ERROR'] = 'Please press the buttons in the given keyboard'
dialogues['GREET2'] = {}
dialogues['GREET2']['text'] = 'Humorous? Me? I am as polite as one can be. But enough about us. Why dont you tell me about you. (*ppst Just thought of telling you all your messages are very secure)' 
dialogues['GREET2']['options'] =[['I am recruiter'], ['I am just checking this out'], ['I am looking for colloboration'], ['I would rather not tell']]
dialogues['GREET3'] = {}
dialogues['GREET3'][dialogues['GREET2']['options'][0][0]] = {}
dialogues['GREET3'][dialogues['GREET2']['options'][1][0]] = {}
dialogues['GREET3'][dialogues['GREET2']['options'][2][0]] = {}
dialogues['GREET3'][dialogues['GREET2']['options'][3][0]] = {}
dialogues['GREET3'][dialogues['GREET2']['options'][0][0]]['text'] = 'Hello recruiter, Before you ask me very specific questions about kowshik, which I really like to answer (most of the times).' 
dialogues['GREET3'][dialogues['GREET2']['options'][1][0]]['text'] = 'Hi there, thanks for your interest. I know you have lot of questions about his profile which I will answer shortly.' 
dialogues['GREET3'][dialogues['GREET2']['options'][2][0]]['text'] = 'Thanks for your interest. I know you have lot of questions about his profile which I will answer shortly.' 
dialogues['GREET3'][dialogues['GREET2']['options'][3][0]]['text'] = 'Thats completely fine by me, I would do the same if I were you. I was designed very carefully to make sure your privacy is not infringed in any manner :)'
dialogues['GREET3']['text2'] = ' Let me just start with most common question:\n who is kowshik chilamkurty?\n Well, he is just a hardwoking professional in AI field. He likes writing, tech and thats one of the reason why he created me. He graduated from prestigious IIT Madras and currently working on Reinforcement Leaning as data scientist in algorithmic trading. I can speak about kowshik all day, you know its my only job for now ;). But'
dialogues['GREET3']['text3'] = 'Would you like to know more about Kowshik Chilamkurty'
dialogues['GREET3']['options'] = [['Yes'],['Someother time']]

dialogues['PROCESS'] = {}
dialogues['PROCESS']['text'] = 'What is that you like to know about him? I would love to answer your questions'
dialogues['PROCESS']['options'] =[['Let me take a look his resume'], ['Can you point me to his writings?'], ['Would love to understand his professional journey'], ['Want to know him more than his CV']]

dialogues['RESUME'] = {}
dialogues['RESUME']['text'] = 'Take a look at his latest resume'

dialogues['WRITINGS'] = {}
dialogues['WRITINGS']['text1'] = 'Kowshik is a prolific writer and Published 35+ innovative and educative blogs on Reinforcement learning, Game Theory, Point Process Models and Survival Models with cumulative viewership of 20K+ views.<a href="https://kowshikchilamkurthy.medium.com">Link</a> for his blog post'
dialogues['WRITINGS']['text2'] = 'His Popular blogs on solving Covid-19 using RL garnered signicant interest from academia, industry and governments for potential collaboration.'
dialogues['WRITINGS']['text3'] = 'Blogs in what topic would you like a take a look at ?'
dialogues['WRITINGS']['options'] = [['Reinforcement learning', 'Game Theory'],
                                    ['Temporal Models','NLP'],
                                    ['History','others'],
                                    [dialogues['reject']]]


dialogues['WRITINGSEND'] = {}
dialogues['WRITINGSEND']['Reinforcement learning'] = '1. <a href="https://towardsdatascience.com/reinforcement-learning-for-covid-19-simulation-and-optimal-policy-b90719820a7f">Reinforcement learning for Covid- 19: Simulation and Optimal Policy</a>\n2.<a href="https://medium.com/mastering-rl-in-minutes">Mastering RL in Minutes: Noisy Networks For Exploration</a>\n3. <a href="https://medium.com/mastering-rl-in-minutes/mastering-rl-in-minutes-a-distributional-perspective-on-reinforcement-learning-124ca327ad2">Mastering RL in Minutes: A Distributional Perspective on Reinforcement Learning</a>\n4. <a href="https://medium.com/mastering-rl-in-minutes/mastering-rl-in-minutes-average-dqn-d8749d0d92a7">Mastering RL in Minutes: Average DQN</a>\n5. <a href="https://medium.com/mastering-rl-in-minutes/mastering-rl-in-minutes-revisiting-fundamentals-of-experience-replay-4c8bec978fd2">Mastering RL in Minutes: Revisiting Fundamentals of Experience Replay</a>\n6.<a href="https://medium.com/mastering-rl-in-minutes/mastering-rl-in-minutes-an-optimistic-perspective-on-offline-rl-70553feda464">Mastering RL in Minutes: An Optimistic Perspective on Offline RL</a>\n7.<a href="https://towardsdatascience.com/wasserstein-distance-contraction-mapping-and-modern-rl-theory-93ef740ae867">Wasserstein Distance, Contraction Mapping, and Modern RL Theory.</a>\n8. <a href="https://towardsdatascience.com/off-policy-vs-on-policy-vs-offline-reinforcement-learning-demystified-f7f87e275b48">Off-policy vs On-Policy vs Offline Reinforcement Learning Demystified!</a>'
dialogues['WRITINGSEND']['Game Theory'] = '1. <a href="https://medium.com/gaming-the-life-game-theory/game-theory-the-prelude-c6fe8791f035">Game Theory: The prelude</a>\n2. <a href="https://medium.com/gaming-the-life-game-theory/game-theory-story-of-thinking-8cde01a436be">Game Theory: Story of Thinking</a>\n3. <a href="https://medium.com/gaming-the-life-game-theory/game-theory-contention-and-cross-effects-c8cc9f6f0af2">Game Theory: Contention and Cross-Effects</a>\n4. <a href="https://medium.com/gaming-the-life-game-theory/game-theory-the-genius-of-nash-3682751c0ee2">Game Theory: The Genius of Nash</a>'
dialogues['WRITINGSEND']['Temporal Models'] = '1. <a href="https://kowshikchilamkurthy.medium.com">Understanding Point Processes</a>\n2. <a href="https://kowshikchilamkurthy.medium.com">Neural Hawkes Process</a>\n3. <a href="https://kowshikchilamkurthy.medium.com">The Cox Proportional-Hazards Model</a>\n4. <a href="https://kowshikchilamkurthy.medium.com">Improve Survival Time in PUBG: A Cox Statistical Approach</a>'


dialogues['WRITINGSEND']['NLP'] = '10. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Bi-Directional LSTM Part(10/40)</a>\n9. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: LSTM Part(9/40)</a>\n8. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Recurrent Neural Networks Basics Part(8/40)</a>\n7. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Training Embeddings using Gensim and Visualisation (Part 7/40)</a>\n6. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Count based Embeddings, GloVe (Part 6/40)</a>\n5. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Dense Representations, Word2Vec (Part 5/40)</a>\n4. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Deep Learning Training Procedure (Part 4/40)</a>\n3. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Deep Learning Theory Basics (Part 3/40)</a>\n3. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Sparse Document Representations (Part 2/20)</a>\n1. <a href="https://kowshikchilamkurthy.medium.com">NLP Theory and Code: Basics (Part 1/20)</a>'


dialogues['WRITINGSEND']['History'] = '1. <a href="https://kowshikchilamkurthy.medium.com">ENLIGHTENMENT</a>\n2. <a href="https://kowshikchilamkurthy.medium.com">American Revolution</a>'
dialogues['WRITINGSEND']['others']  = '1. <a href="https://kowshikchilamkurthy.medium.com">Read this blog before you think you know divisibility completely !</a>'


dialogues['END'] = {}
dialogues['END']['text']  = 'Like to know more about kowshik?'
dialogues['END']['options']  = [['Yes'],[dialogues['reject']]]
dialogues['PROFJOURN'] = {}
dialogues['PROFJOURN']['text1'] = 'Kowshik\'s professional journey was full of ups and downs. He was graduated from IIT Madras in 2018. He developed early Interest in Data science and technology with vision. His professional experience can be categorized into Freelancing, competitions, Internships and publications/patents.'
dialogues['PROFJOURN']['text2'] = 'Which experience would you like to take a look at?'
dialogues['PROFJOURN']['options'] = [['Internships', 'Freelancing'],
                                    ['Competitions','Publications/Patents'],['Open-Source'],[dialogues['reject']]]
dialogues['PROFJOURN']['Internships'] = {}
dialogues['PROFJOURN']['Internships']['text1'] = 'Kowshik worked as intern in different cities around India. He started off as an intern in IIT Bombay in 2nd year winter break and subsequently worked in 4 different companies exhausting every semester break since then. Internships played a very important role in moulding kowshik\'s thought process towards solving a business/research problems. He also filed a patent in one of this internships' 
dialogues['PROFJOURN']['Internships']['text2'] = '<b>Kowshik did his internships in:</b>\n1. Conduent Research Labs, Banglore as Research Intern\n2. Xerox Research Labs, Banglore as Data Science Intern\n3. Nadhi Information Technologies, Chennai as Winter Intern\n4. Light House Analytics, Pune as Data Science Intern\n5. FOSSEE Project, IIT Bombay as Python Intern' 
dialogues['PROFJOURN']['Internships']['text3'] = 'Do you like to checkout what kowshik had done in these internship projects?' 
dialogues['PROFJOURN']['Internships']['options'] = [['Conduent Research Labs, Banglore'],['Xerox Research Labs, Banglore'], ['Nadhi Information Technologies, Chennai'],['Light House Analytics, Pune'],['FOSSEE Project, IIT Bombay'],[dialogues['reject']]]
dialogues['PROFJOURN']['Freelancing'] = {}
dialogues['PROFJOURN']['Freelancing']['text1'] = 'Kowshik\'s early expertise in data science opened a very interesting opportunity for a usual undergraduate student. He completed over 20+ projects rewarded by clients across the globe. He was able to pay his college tution fees with the money earned from freelancing work alone.' 
dialogues['PROFJOURN']['Freelancing']['text2'] = '<b>His very interesting and highly remunerate freelancing opportunities were:</b>\n1. Prediction, NLP, Point Process Models for Unstructured News Data, Client: Metadata.ai Team \n2. Generation of 3D animations for Schrodinger Equation, Client: Fred Rassaii, United Kingdom \n3. Machine Learning and Deep Learning Models for Pixel-Wise classication, Client: Unifie App, India\n4. DNN Models for Educative Adaptive System, Client: Jestha Boyedhur, Mauritius\n5. Feature Engineering for Pharma Text Data, Client: Amit Patel, United Kingdom\n6. Solving Gradients, Client: Sewagi, United Kingdom\n7. ML, NLP Models for Legal Contracts, Client: Vijay Sampathkumar, USA\n7. Vehicle Detection on Highways , Client: Umair, Pakisthan' 
dialogues['PROFJOURN']['Freelancing']['text3'] = 'Do you like to checkout what kowshik had done in these freelancing projects?' 
dialogues['PROFJOURN']['Freelancing']['options'] = [['Prediction, NLP, Point Process Models for Unstructured News Data'],['Generation of 3D animations for Schrodinger Equation'], ['Machine Learning and Deep Learning Models for Pixel-Wise classification'],['Others'],[dialogues['reject']]]
dialogues['PROFJOURN']['Competitions'] = {}
dialogues['PROFJOURN']['Competitions']['text1'] = 'kowshik\'s rich experience in data science is mainly attributed to competition he participated. He competed in more than 20 competitions and won several awards.\nCompetitions exposed him to different businessproblems and various machine learning techniques. He was awarded many PPI\'s from the companies.'
dialogues['PROFJOURN']['Competitions']['text2'] = '<b>Few Important Competitions: </b>\n1. EXL Excellence Quotient-2017, EXL Inc, Delhi \n2. ZS Data-a-thon-2017 ZS Associates, Pune \n3. NASSCOM Competition-2016, NASSCOM, Banglore\n4. Others: Data Mining Cup, GE Healthhack, IT Rajasthan, Zafin Tech, ML-2 by Hackerearth, Analyze This by Amex' 
dialogues['PROFJOURN']['Competitions']['text3'] = 'Do you like to checkout what kowshik had done in these competitions?' 
dialogues['PROFJOURN']['Competitions']['options'] = [['EXL Excellence Quotient-2017'],['ZS Data-a-thon-2017'], ['NASSCOM Competition-2016'],['Others'],[dialogues['reject']]]

dialogues['PROFJOURN']['Publications/Patents'] = {}
dialogues['PROFJOURN']['Publications/Patents']['text1'] = 'Kowshik was very enthusiastic about research and actively published whenever there is an opportunity. Till date Kowshik published 2 research articles and 1 patent.'
dialogues['PROFJOURN']['Publications/Patents']['text2'] = '<b>Publications&Patent: </b>\n1. A Statistical Overview of Sand Demand in Asia and Europe, UKIERI Conference, Goa\n2. Automation of Glass Fragmentation Analysis Using Image Processing, ICCEN 2017, Australia \n3. Modelling Operational Conditions to Predict Life Expectancy and Faults of Vehicle Components in a Fleet, Patent number: USA20200090419, Approved' 

dialogues['PROFJOURN']['Open-Source'] = {}
dialogues['PROFJOURN']['Open-Source']['text1'] = 'Kowshik was very enthusiastic about open source and actively contributes whenever there is an opportunity'
dialogues['PROFJOURN']['Open-Source']['text2'] = '<b>Open Source Projects Maintained By Kowshik: </b>\n1. Reinforcement Learning Annotated Papers\n2. Educative Bot Application'
dialogues['PROFJOURN']['Open-Source']['text3'] = 'Do you like to checkout what kowshik had done in these open source projects?' 
dialogues['PROFJOURN']['Open-Source']['options'] = [['Reinforcement Learning Annotated Papers'],['Educative Bot Application'],[dialogues['reject']]]



dialogues['Internships_state'] = {} 
dialogues['Internships_state']['0'] = '1. Surveyed existing literature to implement a Point Process Algorithm for detection of vehicle faults\n2. Experimented extensively with Neural Hawkes Process and optimized its python implementation'
dialogues['Internships_state']['1'] = '1. <b>Patented the idea of Vehicle-Route Analysis</b> and point process models for fault detection/n2. Best Internship Project - 2nd Runner up. Communicated requirements and results with clients.\n3. Led an initiative to extract insightful features from unstructured data (GPS & Tabular). Employed different methods to detect anomalies in data (PCA, KMeans).\n4. Developed pipelines to integrate large and diverse databases and implemented wide range of Fault Detection Models using extracted features'
dialogues['Internships_state']['2'] = '1. Architected and implemented analytics and machine learning components for nPulse product\n2. Integrated machine learning plugin written in Python into existing Java product code'
dialogues['Internships_state']['3'] = 'Engineered features, selected parameters and calibrated regression models for accurate TRP Ratings Prediction of advertisements for Viacom Inc\n2. Designed an algorithm for Advertisement Schedule Optimization based on TRP rating predictions.I mplemented in Advanced Process OPTimizer (APOPT) software package\n3. Incorporated the Business Constraints of advertisements into schedule optimization algorithm'
dialogues['Internships_state']['4'] = 'Developed and opensourced systematic Python code for solving material mechanics problems'


dialogues['Freelancing_state'] = {} 
dialogues['Freelancing_state']['0'] = '1. Scraped web to collect raw news data. Implemented clustering algorithms(tf-idf) and text feature extraction(Glove Vectors, Parsing)\n2. Conceptualized different ideas to achieve fullest exploitation of textual news data'
dialogues['Freelancing_state']['1'] = '1. Solved 3-D Schrodinger equation in variable time and space setup and interpreted the results in 3D animation in python\n2. Discussed results with client by generating a series of latex files'
dialogues['Freelancing_state']['2'] = '1. Formulated Machine learning algorithms like Gaussian Mixture models, k-Means , one-class SVM and Perceptron algorithms to achieve accurate Pixel-Wise classification\n2. Worked in a cross-functional team to develop U-Net(DNN) model, also explored FCN-32 model'
dialogues['Freelancing_state']['3'] = '1. DNN Models for Educative Adaptive System\n2. Feature Engineering for Pharma Text Data\n3. Solving Gradients\n4. ML, NLP Models for Legal Contracts \n5. Vehicle Detection on Highways'


dialogues['Competitions_state'] = {} 
dialogues['Competitions_state']['0'] = '1. National winners among IIT,NIT\'s to participate in the all-India 3-stage Machine learning challenge\n2. Presented a data driven business solution involving data pre-processing, feature engineering, natural language processing and data modelling\n3. Special mention for visualizing extracted and existing features using a innovative dashboard\n4. Conferred with PPI Offer'
dialogues['Competitions_state']['1'] = '1. Winner in the all-India 2-stage Datathon challenge held in ZS Associates, Pune\n2. Extracted features using glove vectors, sentiment analysis\n3. Developed a prediction model to correctly classify the blog-posts and presented the same\n4. Conferred with PPI Offer'
dialogues['Competitions_state']['2'] = '1. Placed 5th in the all-India 2-stage NASSCOM challenge\n2. Formulated an end-end pipeline to predict the Event/Non-Event of lung cancer\n3. Identified events of lung cancer with F1-score of 0.94 using extreme gradient boosted trees'
dialogues['Competitions_state']['3'] = '1. Data Mining Cup : Placed 2nd in India and Below 50 worldwide 2016,17\n2. GE Healthhack : Placed in top 5 finalist Teams 2017\n3. IT Rajasthan : Placed in top 5 finalist Teams, Opportunity to meet Chief Minister of Rajasthan 2017\n4. Zafin Tech, Kerala : Placed in top 5 finalist Teams 2017\n5. ML-2, Hackerearth : Placed 2th 2017\n6. Analyze This: Amex : Conferred with Honourable Mention'



dialogues['opensource_state'] = {} 
dialogues['opensource_state']['0'] = '1. Compiled and hand annotated 30+ ground breaking Reinforcement Learning research articles\n2. Covered traditional methods like DQN, PG, A2C to advanced topics like Distributional-RL, Offine Policy Learning and Deep Deterministic Methods'
dialogues['opensource_state']['1'] = '1. Innovated an End-to-End bot application in Python to handle Ed-Tech customer in telegram mobile application\n2. Designing NLP and ML course track (25 percent completed) for testing the bot usage in effective content dispersal'


dialogues['PERJOURN'] = {}
dialogues['PERJOURN']['text1'] = 'Kowshik is highly motivated individual. He loves writing and reading. He likes to spend his time in a very organized way. His inclinations towards liberals ideas renders very a calm outlook towards matters.'
dialogues['PERJOURN']['text2'] = 'Go on, click on a question to understand kowshik\'s persona'

dialogues['PERJOURN']['options'] = [['1. What are his thoughts towards religious matters?'],
                                    ['2. What he think is very mort important in life?'],
                                    ['3. Whats his approach towards learning new topics?'],
                                    ['4. Who inspired kowshik ?'],
                                    ['5. What\'s kowshiks approach towards competition and failure?'],[dialogues['reject']]]


dialogues['PERJOURN']['0'] = 'Thanks for asking.\n  Kowshik is a very practical person and doesn\'t neither have any strict religious beliefs nor an atheist. He still agrees to participate in religious rituals as a matter of fact. Being a global citizen, he not only respect others religious feelings but also defends if required.'
dialogues['PERJOURN']['1'] = 'Thanks for asking.\n  Kowshik believes that 2 most important things in life are appreciation and feedback. One needs to get appreciation, if he deserves for his actions. Feedback, he thinks is Absolutely important in very aspect of life. Everything including relationships must have very solid feedback loops for success. '
dialogues['PERJOURN']['2'] = 'Kowshik loves getting familiar with different subjects he encounter. He believes books and research articles are very reliable sources and usually prefers self-paced learning unlike many courses offer.'
dialogues['PERJOURN']['3'] = 'Yes, two of Kowshik\'s college professors inspired him.\nManu Santhanam, with whom kowshik published his first research article. prof. Manu\'s approach towards teaching and research deeply influenced kowshik.\nProf. Arul Jayachandhran also working as professor in IIT Madras, with whom kowshik published his 2nd research article. His selfless natural and his commitment towards student\'s overall improvement inspired kowshik deeply. Prof. Arul will continue to inspire his students and he will never be forgotten by those who knew him.'
dialogues['PERJOURN']['4'] = 'Kowshik likes to be challenged, but always perceives it an opportunity to learn and get a feedback. That\'s one of the reasons, he competed in 20+ AI/ML competitions. He believes that success is never a sole measurement of happiness, we should derive happiness from the amount of hardwork and passion.'
 

dialogues['GREET1']['acceptable'] = ['Yes, Ofcourse', 'No, Some other time']
dialogues['GREET2']['acceptable'] = ['I am recruiter', 'I am just checking this out', 'I am looking for colloboration', 'I would rather not tell']
dialogues['GREET3']['acceptable'] = ['Yes','Someother time']
dialogues['PROCESS']['acceptable'] =['Let me take a look his resume', 'Can you point me to his writings?', 'Would love to understand his professional journey', 'Want to know him more than his CV']   
dialogues['WRITINGS']['acceptable'] = ['Reinforcement learning', 'Game Theory','Point Process Models','Survival Models','History','others',dialogues['reject'],'Temporal Models','NLP']
dialogues['PROFJOURN']['acceptable'] = ['Internships', 'Freelancing', 'Competitions','Publications/Patents','Open-Source',dialogues['reject']]
dialogues['PERJOURN']['acceptable'] =  ['1. What are his thoughts towards religious matters?',
                                    '2. What he think is very mort important in life?',
                                    '3. Whats his approach towards learning new topics?',
                                    '4. Who inspired kowshik ?',
                                    '5. What\'s kowshiks approach towards competition and failure?',dialogues['reject']]
dialogues['Internships_state']['acceptable'] = ['Conduent Research Labs, Banglore','Xerox Research Labs, Banglore', 'Nadhi Information Technologies, Chennai','Light House Analytics, Pune','FOSSEE Project, IIT Bombay',dialogues['reject']]
dialogues['Competitions_state']['acceptable'] = ['EXL Excellence Quotient-2017','ZS Data-a-thon-2017', 'NASSCOM Competition-2016','Others',dialogues['reject']]
dialogues['opensource_state']['acceptable'] = ['Reinforcement Learning Annotated Papers','Educative Bot Application',dialogues['reject']]
dialogues['Freelancing_state']['acceptable'] = ['Prediction, NLP, Point Process Models for Unstructured News Data','Generation of 3D animations for Schrodinger Equation', 'Machine Learning and Deep Learning Models for Pixel-Wise classification','Others',dialogues['reject']]
