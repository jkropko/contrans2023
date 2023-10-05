# Transparency Dashboard for the U.S. Congress
## Description
The purpose of this dashboard is to compile data from public sources on the voting, bill sponsorship, committee work, and financial contributions of members of the U.S. House of Representatives and Senate.

Compiled as a class project for DS 6600: Data Engineering 1 in the Ph.D. program in Data Science at the University of Virginia.

# Raw data documentation

  * [Congressional Ideology Data](https://htmlpreview.github.io/?https://github.com/jkropko/contrans2023/blob/main/congress_ideology.html)

  * [Congressional Votes Data](https://htmlpreview.github.io/?https://github.com/jkropko/contrans2023/blob/main/congress_votes.html)

  * [Individual members' votes](https://htmlpreview.github.io/?https://github.com/jkropko/contrans2023/blob/main/member_votes.html)

  * [House of Reps Elections Data](https://htmlpreview.github.io/?https://github.com/jkropko/contrans2023/blob/main/elections_house.html)
  
  *[Congress Bills](https://jsonhero.io/j/QY2ZJEssznf8)
  
# Datasets and key variables:

### Voteview: individual members' votes:

  * congress (filter)
  * chamber
  * rollnumber [pk]
  * icpsr [pk]  
  * cast_code
  
 ### Voteview: Congressional ideology data
 
   * congress (filter)
   * chamber
   * icpsr [pk]
   * state_abbrev
   * district_code
   * party_code
   * bioname
   * bioguide_id
   * nominate_dim1
   
 ### MIT Election data: House
 
   * year (filter)
   * stage (filter)
   * state_po [pk]
   * district [pk]
   * candidate [pk]
   * party
   * candidatevotes
 
 ### MIT Election data: Senate
 
   * year (filter)
   * stage (filter)
   * district [pk]
   * candidate [pk]
   * party
   * candidatevotes 
   
 