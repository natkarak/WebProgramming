Library
==========
### Web Programming project, winter semester 2016

##### Project topic (translated)
Genovefa has quite a large and interesting collection of books at home. Despite the emergence of all kinds of electronic readers, she believes that the paper has still its charm (it is easier keep a broken table in balance with the help of book than with Kindle). Genovefa's collection of books is appreciated by her friends, because in this way they can get to bestsellers better than in the library. Unfortunately, Genovefa significantly better remember the content of books than a person who has a book borrowed.

Help her to solve her problem with a web application that will remember all of the book collection. The application allows the entry of a new book (any book being entred gets its unique number).

In addition, the app also allows you to record the records of the loan (ie, who borrowed which book and when). History of rentals for a single book should be maintained.

Genovefa's friends could enable search in the database of books(if a book is borrowed or not).

The application should be written in a way that will allow the rental of other things (eg. CDs, tools, ...)

#####Target audience and devices
Target audience of this web application includes everybody that loves to read book (in the paper form) and does not mind using computer to keep track of his/hers borrowed books.
As for the tagret devices: are a computer and a mobile phone (to help the user controlling his books even on the road) and for completness is added also a tablet version.

######Issues concerning different browsers
The web application was built referencing Google Chrome.
One of the issues is the video plugin on the homepage. 
This plugin does not work very well on Mozila Firefox - it is not getting smaller when the window is being shrunk (not just the element, but it prevents whole aside part from becoming smaller), therefore the responsivity is slightly worse here.
But it was tested also on the Microsoft Edge and Google Chrome - on these two there is no problem with it.

Other than that no significat differences and issues were find in comparison of the web browsers.

######Problems to solve and comments
Things that need to be solved: 
-how to give permission to some things only to the administrator- django permissions,
-sending of the forms,
-accordion on dashboard still does not work.

I have put a lot of effort to create the main page- to make it look somewhat representative 
(in case of showing it to someone that does not know it is for a school project might think about signinup), 
but also because this is the page where I was testing and fixing majority of the components of the page.
The second one I would say the fact of how the page works on different screen sizes.


*Author:
Natália Rakovská, 23.10.2016
