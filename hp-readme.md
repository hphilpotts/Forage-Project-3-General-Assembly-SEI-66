# Pinterest-type App - Django-SQL       

## GA London SEI-66 Project 3: Django Framework, postgreSQL Database         

_Rough notes of process to be converted to a lovely readme at a later date!_        

## Planning Stage 1, Day 01:        
29/09/22        

Team formed: Helene (Team Lead), Ivan and I. We have decided on a 'Pinterest-type' app for our project.     

### Early Planning stages:      
We have set up a Trello board to manage workflow, established a main Repo and forked successfully to Team Members. This has been something of a learning curve - having been Team Lead on the previous group project I have had to get used to the extra steps required when forking!           

Early Wireframe completed and ERD started. Advice taken on how to relation our tables. At one stage, we were deciding between a three-table join table (User, Image, Board) and three join tables. Eventually we decided upon a single join table for Image-Board M-M and 1-M for User-Image and User-Board.

## Planning Stage 2, Day 02:        
Site roadmap set up in Excel document,      

[add rest of Day 02 here]       

## Production Stage 1, Day 03:      

Decided to extend built-in Django User model by adding User Profile model linked One-One. Not yet tested working as Auth fnc. has not been added at this stage. Model added to `models.py`, with image upload fnc which will need to be tweaked once testing can begin.     
Created database in _pgAdmin4_ and successfully migrated, checked working ok in GUI.        

Starting on auth route. We'll need to go back later and update this path to a more interesting page than 'Home' one the right paths are set up. I've added this to Trello Board so that this doesn't get missed! Ditto `redirect` path in `signup` view.        

[git struggles in here]     

User details page added: R from Read!