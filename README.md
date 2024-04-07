# Demos and code associated with doctoral research

Implementaion of ideas contained in the paper [Why try to build try to build a co-creative poetry system that makes people feel that they have “creative superpowers”?](https://ceur-ws.org/Vol-3359/paper8.pdf)

The paper and its related experiments examine (i) state-of-the-art writing assistants; (ii) LLM vs human contribution for writing tasks and (iii)  SOTA vs custom writing assistants
The key experimental contribution of the paper is the *SParse And Dense Network Model* The system operates as a Sparse And Dense Network (SPaD). 

# SPaD Design 
The name refers to the system being sparse with respect to user input tokens as compared to tokens contained in the LM/LLMs. Against this, the system is dense in terms of leveraging transformer models and their associated attention layers.  The intuition is to use a small amount of personalized user text to attempt to customize the output of powerful LMs/LLMs.
 
# Model Elements
1. Text input by user is returned as partially completed poetic text and/or poetic and lyrical recommendations for the user to consider. 

2. User personalized data submitted as poems or lyrics and/or recommendations of favourite artists and their work. These are used to create a corpus of user text. Prior
examples of user generated text uploaded to system; recommender and/or database search to enhance user text with additional poetic texts (e.g from web crawl) 

3. Database of poetic texts (and song lyrics) from web crawl. Clean text is included as well as metadata such as rhyme scheme and Parts of Speech (PoS).

# Differences to Current LLMs
*State-of-the-Art LLMs* form part of the SPaD in order to help improve the SPAD’s performance; in other words, the LLMs are source of input training data and as such multiple LLMs could in theory be included in the SPaD architectural design.

*Poetry specific Language Model* forms part of the design; poetry specific refers to adaptations to the underlying model architecture in order that token processing and output is more optimal with respect to poetry than prose. An example of this might be applying additional linguistic layers within the network to favour text strings
with syllable frequencies found more regularly in poems than say news articles or web pages. Although architecture is referred to, much of any benefit at this stage might come from modifying the training data and associated recipes. The poetry specific LLM would also leverage data from the general LLM (for simplicity any interaction between the two elements is not included)

Poetry Language Model is a custom model whose network architecture and training data are adapted for poetry. 

As well as providing a data contrast to the LLMs, the SPaD  will also act as a style transfer layer in so far as it identifies and tries to modify input text to create poetic styles. These styles will be mapped onto user styles upstream within the system.

The result of the models described above, is a system that contains information on generalized poetic style as well as individual style preference(s) unique for each user. This allows the system to support users with specific co-writing tasks (e.g text generation) as well as offer personalized recommendations for further reading of relevant poems and/or poets. 

# SPaD Design Goals

In user experience terms, this might be delivered via an interface that allows the user
to switch between: (a) writing text, (b) editing generated and  (c) reading and reflecting on specific poetic recommendations made by the system.

Develop sense of of generalized poetic language plus  individual style preference(s) unique for each user.

Support co-writing tasks such as text generation.

Offer targeted recommendations for further reading. 

Allow switching between writing, editing generated text, and browsing recommendations.


# Implementation

System would have a number of states that range from full automation to text prompts acting as a starting point for the user. The support states envisaged are:

1. State-A: general language system implemented as standard.

2. State-B: general language system implemented with modified architecture to include user generated content within training set and/or network architecture preferences.

3. State-C: poetry specific system implemented with standard architecture.

4. State-D: poetry specific system implemented with modified architecture to include user generated content within training set and/or network architecture preferences.

The LLM component of the system would use publicly available APIs and where possible, modify network architecture directly. Ideally a custom poetry and lyric language model would be implemented; aside from practicalities, there is a technical challenge in that a poetry and lyric LM would be far smaller than a general LLM. Given the research on LLM size and performance, a custom poetry and lyric LM would in theory therefore under perform against state-of- the-art LLMs. 

# Experiments

The system would run a number of experiments with the purpose of establishing which system components most support users to write “better” poetry; in goal terms,
better is evaluated:

</br>(a) subjectively by users via a Likert scale and </br>
(b) by performance on related tasks such as the Divergent Action Task or
</br>(c) Bridge-the-Associative-Gap Task, or rhyme creation and identification </br>

The tasks would be completed external to the system. The goals of the evaluation are to measure to what extent users are actually improving their poetry writing abilities, and the degree to which any improvement is as a result of internal system features. For a user, improvement is concerned with "the writer’s goals or their desire to have an individual voice". With this as a basis, the evaluation process takes the form of a number of hypotheses and related experiments, the purpose of which is to explore; 

(a) how well general vs poetry specific language models can write full poems;
(b) if poetry specific language models can better represent individual users style than generalized language models; and, 
(c) the extent to which system recommendations help users when they write 
poems 

The hypotheses and experiments are concerned with poetic text style which describes the ways (an author) uses language, including prosody, word choice, sentence structure and use of figurative language

*1. Hypothesis-A* that poetry specific language generation could outperform general language generation with respect to creating poems.

*Experiment A:* each system-state generates complete poetic texts. The prompts would also be given to users (inexperienced and advanced) with the same constraints as the system in terms of keywords, topics, character limits etc.

The evaluation for experiment A is by humans who judge the quality of the poems (which are anonymous) by a Likert scale and free text summary.

*2. Hypothesis-B* that poetry specific language generation customized for a given user could outperform vanilla poetry specific generation with respect to creating poems. 

*Experiment B:* each system state generates complete poetic text but some states are pre-trained to customize characteristics with respect to given users and their poetic styles. 

The evaluation for experiment B is by humans who judge the quality of the poems by a Likert scale and free text summary.

The evaluation is focused on how well the poems represent the given users’ individual style.

*3. Hypothesis-C* that external recommendations, full or part poems, based on given user characteristics are supportive with respect to users writing their poems. 

*Experiment C:* for given users generated poetic text inputs, the system state generates (external to system) poetic text recommendations that the user reads and reflects on before completing their poem. 

The evaluation for experiment C is by humans who judge how well the poem
recommendations helped them write poems in the theme, topic or style they were attempting to achieve.

A central challenge for the proposed system is that the development and attainment of an individual poetic voice is highly subjective. Beyond subjectivity, poetry is from a societal perspective often a question of cultural value which over time may well change.

The approach described provides a sense of how user activities (internal and external) with respect to the system can be evaluated. In practice, more fine-grained
evaluation criteria would be required based on further research and operational or implementation design; as far as possible, a complete system would have an awareness of all relevant evaluation data including for instance, external system reading of poems. At this stage, the evaluation proposed is limited to the extent necessary in order to support the explanation of how and why the system might work. 





    

