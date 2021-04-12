# Fade to Black: Predicting How Long a Show Will Run On Broadway



## Project Overview:
Can I build a predictive model that imporves upon the baseline accuracy model for predicting how long a show on Broadway will run?
To answer this question, I will acquire, prepare, and explore data to identify those feaures of braodway shows that drive the the target, length of run. 


## Initial Questions
- Does show type (Musical, Play, etc.) affect how long a show will run?
- Does the number of performers in the show affect run time?
- Does venue influence a show's success as defined by how long the show runs? 


## Key Findings

- The best **drivers** for predicting how long a show will run on Broadway are:
    - If the show is a musical
    - If the show is a play
    - The number of creative team members working on the show
    - The number of performers working on the show
    - The total number of people working on the show
<br>  
<br>
- The **baseline model** for predicting how long a show runs has an root mean square error of 367 days.
<br>  
<br>    
- I have built a **Generalized Linear Model** that **improves** upon the baseline model by 46% on out of sample data.
    - This model is better than not having a model at all! The root mean square error is 200 days for the GLM model. 
<br>  
<br>   
- With more time and data, I am confident this model can be improved upon. 


## Data Dictionary

| Target| Description | Data Type |
|---------|-------------|-----------|
| 'length_of_run' | The total number of days a show was open in a Broadway playhouse| int64 |

| Features | Description | Data Type |
|---------|-------------|-----------|
| 'year' | When the show opened on Broadway  | int64 |
| 'N people' | Indicates the number of people (performers and creative team) that worked on the show| int64 |
| 'N performers' | Indicates the number of performers in the show | int64 |
| 'N creative team' | Indicates the number of people on the creative team (non performers)| int64 |
| 'theatre_id' | Unique id for the theatre where the show was mounted| int64 |
| 'Theatre Capacity' | The audience capacity for the show per performance | int64 |
| 'Production_Type_Concert' | Show is classified as a concert  | uint8 |
| 'Production_Type_Original_Production' | Show is classified as an original production at time  | uint8 |
| 'Production_Type_Premiere' | Indicates if it is the first iteration and mounting of the show  | uint8 |
| 'Production_Type_Revised_Production' | Indicates if the show is revised from an original iteration  | uint8 |
| 'Production_Type_Revival' | Indicates if the show titled has previously opened and closed on broadway at least one other time  | uint8 |
| 'Show_Type_Ballet' | Genre of show is classified as Ballet  | uint8 |
| 'Show_Type_Dance' | Genre of show is Dance (non Ballet) | uint8 |
| 'Show_Type_Musical' | Genre of show is musical  | uint8 |
| 'Show_Type_One-Acts' | Genre of show is one-act show; typically shorter in length than a full-length play and usually staged without an intermisson  | uint8 |
| 'Show_Type_Opera_Bouffe' | Show is a French Comic Opera  | uint8 |
| 'Show_Type_Operetta' | Show is a 'light opera' and includes dialogue, some music and dance  | uint8 |
| 'Show_Type_Other' | The show does not fall into another category or may be multi-category genre  | uint8 |
| 'Show_Type_Performance' | Performance art / avant garde  | uint8 |
| 'Show_Type_Play' | Indicates a play with limited or no music  | uint8 |
| 'Show_Type_Play_with_music' |  A show that utilizes music, but the performers utilize more dialogue than singing| uint8 |
| 'Show_Type_Solo' | One peformer show   | uint8 |
| 'Show_Type_Vaudeville' | The show is stylistically that of the 20th century variety show / burlesque genre  | uint8 |



## Steps for Replication
1. Read this README
2. Download .csv file in repo
3. Duplicate the following moduels from repo:
    - acquire.py
    - prepare.py
    - explore.py
    - evaluate.py
4. Open Final_Report in this repo and run all cells


