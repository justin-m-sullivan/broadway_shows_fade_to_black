# Fade to Black: Predicting How Long a Show Will Run On Broadway



## Project Overview:
Can I build a predictive model that imporves upon the baseline accuracy model for predicting how long a show on Broadway will run?
To answer this question, I will acquire, prepare, and explore data to identify those feaures of braodway shows that drive the the target, length of run. 

## Table of Contents


## Initial Questions
- Does show type (Musical, Play, etc.) affect how long a show will run?
- Does the number of performers in the show affect run time?
- Does venue influence a show's success as defined by how long the show runs? 


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
| 'Production_Type_Concert' |   | uint8 |
| 'Production_Type_Original_Production' |   | uint8 |
| 'Production_Type_Premiere' |   | uint8 |
| 'Production_Type_Revised_Production' |   | uint8 |
| 'Production_Type_Revival' |   | uint8 |
| 'Show_Type_Ballet' |   | uint8 |
| 'Show_Type_Dance' |   | uint8 |
| 'Show_Type_Musical' |   | uint8 |
| 'Show_Type_One-Acts' |   | uint8 |
| 'Show_Type_Opera_Bouffe' |   | uint8 |
| 'Show_Type_Operetta' |   | uint8 |
| 'Show_Type_Other' |   | uint8 |
| 'Show_Type_Performance' |   | uint8 |
| 'Show_Type_Play' |   | uint8 |
| 'Show_Type_Play_with_music' |   | uint8 |
| 'Show_Type_Solo' |   | uint8 |
| 'Show_Type_Vaudeville' |   | uint8 |



## Steps for Replication
