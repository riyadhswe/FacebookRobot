from os import system
from GroupInvite import GroupInvite
from GroupReact import GroupReact
from GroupComments import GroupComments
from ReactTimeline import ReactTimeline
from CommentsTimeline import CommentsTimeline
from ReactCommentsTimeline import ReactCommentsTimeline
from Hahareact import hahareact
from day import ReactDay



def main():
    system('cls')
    print("................Facebook Robot................")
    print("     0. [Group]Invite People           ")
    print("     1. [Group]React                   ")
    print("     2. [Group]Comments                ")
    print("     3. [TimeLine]React                ")
    print("     4. [TimeLine]Comments             ")
    print("     5. [TimeLine]React and Comments   ")
    print("     6. [TimeLine]Haha Attack          ")
    print("     7. [Day]Love  react               ")
    print("..............................................")
    choice = int(input("Enter your choice : "))
    operation = [GroupInvite,GroupReact,GroupComments,ReactTimeline,CommentsTimeline,ReactCommentsTimeline,hahareact,ReactDay]
    operation[choice]()
    main()

main()
